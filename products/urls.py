from django.urls import path
from .views      import (
                    ProductListAPIView,
                    ProductDetailView,
                    WishlistCreateView,
                    WishlistDestroyView
                    )

urlpatterns = [
    path('',ProductListAPIView.as_view(),name='productlist'),
    path('<int:product_id>',ProductDetailView.as_view(),name='productdetail'),
    path('<int:product_id>/wishlists',WishlistCreateView.as_view(),name='wishlist_create'),
    path('<int:product_id>/wishlists/<int:wishlist_id>',WishlistDestroyView.as_view(),name='wishlist_delete'),
]
