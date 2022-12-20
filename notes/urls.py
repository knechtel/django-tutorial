from django.urls import path
from . import views

urlpatterns = [
    path('notes/', views.list),
    path('login-end/', views.login),
    path('login', views.LoginInterfaceView.as_view()),
    path('logout', views.LogoutInterfaceView.as_view()),
    path('signup', views.SignupView.as_view(), name='signup'),
]
