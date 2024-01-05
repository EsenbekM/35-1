from django.urls import path

from post import views


urlpatterns = [
    path('', views.main_view),
    path('posts/', views.post_list_view),
    path('posts/create/', views.posts_create_view),
    path('posts/<int:post_id>/', views.post_detail_view),
    path('posts/<int:post_id>/update/', views.post_update_view),
    path('posts/<int:post_id>/comment/create/', views.comment_create_view),
    path('hashtags/', views.hashtag_list_view),

    path('comments/', views.CommentListView.as_view()),
    path('comments/create/', views.CommentCreateView.as_view()),
    path('comments/<int:comment_id>/', views.CommentDetailView.as_view()),
    path('comments/<int:comment_id>/update/', views.CommentUpdateView.as_view()),
]
