from django.urls import path
import products.views


urlpatterns = [
    path("detail/<int:product_id>", products.views.product_detail, name="product_detail"),
    path("shopping", products.views.shopping_cart, name='shopping_cart'),
    path('add_to_cart/<int:product_id>', products.views.add_to_cart, name="add_to_cart"),
    path('remove-cart/<int:cart_id>', products.views.remove_cart_item, name='remove_cart_item')
] 