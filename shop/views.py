from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, EmptyPage,InvalidPage
from django.db.models import Q
from . models import *
# Create your views here.
              
def index(request):
    prod = products.objects.all().order_by('id')[:9]
    paginator = Paginator(prod, 6)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        product = paginator.page(page)
    except (EmptyPage, InvalidPage):
        product = paginator.page(paginator.num_pages)
    return render(request, 'index.html', {'prod': product})

def product(request, categ_slug = None):
    c_page = None
    prod = None
    if categ_slug != None:
        c_page = get_object_or_404(category, slug = categ_slug)
        prod = products.objects.filter(category = c_page, available=True).order_by('id')
    else:
        prod = products.objects.all().filter(available = True).order_by('id')

    paginator = Paginator(prod, 6)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        product = paginator.page(page)
    except (EmptyPage, InvalidPage):
        product = paginator.page(paginator.num_pages)
    categ = category.objects.all().order_by('id')
    return render(request, 'products.html', {'prod': product, 'categ': categ})

def prodDetails(request, categ_slug, prod_slug):
    try:
        prod = products.objects.get(category__slug = categ_slug, slug = prod_slug)
    except products.DoesNotExist:
        prod = None
        print(f"No product found for category slug '{categ_slug}' and product slug '{prod_slug}'")
    return render(request, 'product-detail.html', {'prod': prod})

def searching(request):
    prod = None
    query = None
    mess = None
    if 'query' in request.GET:
        query = request.GET.get('query')
        prod = products.objects.all().filter(Q(name__icontains = query) | Q(desc__icontains = query))
        if not prod:
            mess = "No products found matching your search"
    
    paginator = Paginator(prod, 6)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        product = paginator.page(page)
    except (EmptyPage, InvalidPage):
        product = paginator.page(paginator.num_pages)

    return render(request, 'search.html', {'qr': query, 'prod': product, 'mess': mess})

def men(request):
    prod = products.objects.filter(category__name='Men', available=True).order_by('id')

    paginator = Paginator(prod, 6)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        product = paginator.page(page)
    except (EmptyPage, InvalidPage):
        product = paginator.page(paginator.num_pages)

    return render(request, 'men.html', {'prod': product})

def women(request):
    prod = products.objects.filter(category__name='Women', available=True).order_by('id')

    paginator = Paginator(prod, 6)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        product = paginator.page(page)
    except (EmptyPage, InvalidPage):
        product = paginator.page(paginator.num_pages)

    return render(request, 'women.html', {'prod': product})

def kids(request):
    prod = products.objects.filter(category__name='Kids', available=True).order_by('id')

    paginator = Paginator(prod, 6)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        product = paginator.page(page)
    except (EmptyPage, InvalidPage):
        product = paginator.page(paginator.num_pages)

    return render(request, 'kids.html', {'prod': product})
