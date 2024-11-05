from django.urls import path

from app_product import views


urlpatterns = [
    path('', views.ProductListForUserView.as_view()),
    path('admin/', views.ProductListForAdminView.as_view()),
    path('admin/<int:pk>/', views.ProdictDetailForAdminView.as_view()),
]
