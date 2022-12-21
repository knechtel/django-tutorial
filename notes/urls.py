from django.urls import path
from . import views

from django.contrib.auth import views as auth_views
urlpatterns = [
    path('notes/', views.list, name='notes'),
    path('login-end/', views.login),
    path('login/', views.LoginInterfaceView.as_view(), name='login'),
    path('logout', views.LogoutInterfaceView.as_view()),
    path('signup', views.SignupView.as_view(), name='signup'),

]
