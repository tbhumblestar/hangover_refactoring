from django.urls    import path
from products.views import (
                        WishlistUserListView,
                        ReviewUserListView,
                    )
from .views         import (
                        KaKaoLoginView,
                        KaKaoLogOutView,
                        UserDetailView,
                    )

urlpatterns = [
    #기능이 다 정해지면 auth라는 클래스에 맵퍼함수를 만들어서 한번에 처리할 수 있도록 해볼 것
    path('kakaologin',KaKaoLoginView.as_view(),name='kakaologin'),
    path('kakaologout',KaKaoLogOutView.as_view(),name='kakaologout'),
    path('<int:user_id>',UserDetailView.as_view(),name='UserDetail'),
    path('<int:user_id>/wishlists',WishlistUserListView.as_view(),name='UserWishlists'),
    path('<int:user_id>/reviews',ReviewUserListView.as_view(),name='UserReviews'),
]
