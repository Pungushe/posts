from django.urls import path

from  . import views

urlpatterns = [
    # главная страница
    path('', views.main_post, name='post'),
    # посты
    path('category/<tag>/', views.main_post, name='post-category'),
    path('post/create/', views.post_create, name='post-create'),
    path('post/delete/<pk>/', views.post_delete, name='post-delete'),
    path('post/edit/<pk>/', views.post_edit, name='post-edit'),
    path('post/<pk>/', views.post_page, name='post-page'),
    path('post/<pk>/like/', views.like_post, name='like-post'),
    # комментарии
    path('commentsent/<pk>/', views.comment_sent, name='comment-sent'),
    path('comment/<pk>/', views.comment_delete, name='comment-delete'),
    path('reply-sent/<pk>/', views.reply_sent, name='reply-sent'),
    path('reply/delete/<pk>/', views.reply_delete, name='reply-delete'),
    # лайки
    path('post/like/<pk>/', views.like_post, name='like-post'),
    path('comment/like/<pk>/', views.like_comment, name='like-comment'),
    path('reply/like/<pk>/', views.like_reply, name='like-reply'),
]
