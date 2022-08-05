from django.contrib import admin
from django.urls    import path,include,re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg       import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="HangOver Project \n\n API description",
      default_version='refactoring',
      description="Get을 제외한 모든 메서드는 JWT토큰을 보내야 합니다",
    #   terms_of_service="https://www.google.com/policies/terms/",
    #   contact=openapi.Contact(email="contact@snippets.local"),
    #   license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/',include('users.urls')),
    path('products/',include('products.urls')),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    ]
