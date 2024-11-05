from django.urls import path

from app_comment import views


urlpatterns = [
    path('', views.CommentListView.as_view()),
    path('<int:pk>/', views.CommentDetailView.as_view()),
]