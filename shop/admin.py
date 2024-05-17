from django.contrib import admin
from . models import category, products

# Register your models here.
class categoryadmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(category, categoryadmin)


class productsAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'stock']
    list_editable = ['price', 'stock']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(products, productsAdmin)
