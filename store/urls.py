from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('category/<slug:category_slug>', views.home, name='products_by_category'),
    path('category/<slug:category_slug>/<slug:product_slug>', views.productPage, name='product_detail'),
    path('product/', views.productPage, name='product'),
    path('search/', views.search, name='search'),
    path('cart', views.cart_detail, name='cart_detail'),
    path('cart/add/<int:product_id>', views.add_cart, name='add_cart'),
    path('cari/remove/<int:product_id>', views.cart_remove, name="cart_remove"),
    path('cari/remove_product/<int:product_id>', views.cart_remove_product, name="cart_remove_product")
]
