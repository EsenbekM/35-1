from django.urls import path

from post import views


urlpatterns = [
    path('', views.main_view),
    path('posts/', views.post_list_view),
    path('posts/create/', views.posts_create_view),
    path('posts/<int:post_id>/', views.post_detail_view),
    path('hashtags/', views.hashtag_list_view),
]
