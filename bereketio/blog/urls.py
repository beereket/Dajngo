from django.urls import path
from . import views


urlpatterns = [
    # path('', views.home, name="blog-home"),
    path('about/', views.about, name="blog-about"),
    path('', views.PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='blog-post'),
    path('post/new/', views.PostCreateView.as_view(), name='blog-new'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='blog-update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='blog-delete'),
    path('post/<int:pk>/comment/', views.CommentCreateView.as_view(), name='blog-comment'),
]
