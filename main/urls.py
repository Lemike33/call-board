from django.urls import path
from . import views

urlpatterns = [
    path('', views.ShowPostView.as_view(), name='home'),
    path('post/<int:pk>', views.DetailPostView.as_view(), name='post-detail'),
    path('post/add', views.CreatePostView.as_view(), name='post-add'),
    path('comment/add', views.CreateCommentView.as_view(), name='comment-add'),
    path('post/<int:pk>/update', views.UpdatePostView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', views.DeletePostView.as_view(), name='post-delete'),
]
