from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('api/example/', views.example_view, name='list'),
    path('api/v1/', views.NotesList.as_view(), name='list'),
    path('api/v1/new', views.NotesCreate.as_view(), name='create'),
    path('notes/', views.list, name='notes'),
    path('login-end/', views.login),
    path('login/', views.LoginInterfaceView.as_view(), name='login'),
    path('logout', views.LogoutInterfaceView.as_view()),
    path('signup', views.SignupView.as_view(), name='signup'),
]
