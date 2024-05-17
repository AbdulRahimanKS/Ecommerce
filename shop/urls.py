from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('mens/', views.men, name='men'),
    path('womens/', views.women, name='women'),
    path('kidss/', views.kids, name='kids'),
    path('product/', views.product, name='product'),
    path('<slug:categ_slug>/', views.product, name='prodcat'),
    path('<slug:categ_slug>/<slug:prod_slug>', views.prodDetails, name='prod-detail'),
    path('search', views.searching, name='search')
]
