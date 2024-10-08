from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register, name="users-register"),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name="users-login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name="users-logout"),
    path('profile/', views.profile, name="users-profile"),
    path('profile-update/', views.profile_update, name="users-profile-update"),
    path('follow/<str:username>/', views.follow_user, name='follow-user'),
    path('unfollow/<str:username>/', views.unfollow_user, name='unfollow-user'),
]