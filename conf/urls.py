from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('app_user.urls')),
    path('api/product/', include('app_product.urls')),
    path('api/comment/', include('app_comment.urls')),
]
