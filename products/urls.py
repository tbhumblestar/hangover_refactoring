from django.urls import path
from .views      import (
                    ProductListAPIView,
                    ProductDetailView,
                    WishlistCreateView,
                    WishlistDestroyView,
                    ReviewCreateView,
                    ReviewdetailView,
                    ProductSearchView
                    )

urlpatterns = [
    path('',ProductListAPIView.as_view(),name='productlist'),
    path('<int:product_id>',ProductDetailView.as_view(),name='productdetail'),
    path('<int:product_id>/wishlists',WishlistCreateView.as_view(),name='wishlist_create'),
    path('<int:product_id>/wishlists/<int:wishlist_id>',WishlistDestroyView.as_view(),name='wishlist_create'),
    path('<int:product_id>/reviews',ReviewCreateView.as_view(),name='review_create'),
    path('<int:product_id>/reviews/<int:review_id>',ReviewdetailView.as_view(),name='review_delete'),
    path('search',ProductSearchView.as_view(),name='search'),
]
