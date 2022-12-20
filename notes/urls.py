from django.urls import path
from . import views

urlpatterns = [
    path('notes/', views.list),
    path('login-end/', views.login),
    path('login', views.LoginInterfaceView.as_view()),
]
