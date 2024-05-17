from django.urls import path
from . import views

urlpatterns = [
    path('cartDetails/', views.cart_details, name='cartDetails'),
    path('add/<int:product_id>/', views.add_cart, name = 'addcart'),
    path('min/<int:product_id>/', views.min_cart, name = 'mincart'),
    path('del/<int:product_id>/', views.del_cart, name = 'delcart')
]
