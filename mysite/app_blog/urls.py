from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('create-article/', views.create_article, name='create_article'),
    path('delete-post/<int:post_id>/', views.delete_post, name='delete_post'),
]