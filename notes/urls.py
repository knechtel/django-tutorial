from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('api/example/', views.example_view, name='list'),
    path('api/v1/', views.NotesList.as_view(), name='list'),
    path('api/v1/new', views.NotesCreate.as_view(), name='create'),
    path('api/v1/equipment/', views.EquipmentList.as_view(), name='list-equipment'),
    path('api/v1/equipment/new/', views.EquipmentCreate.as_view(),
         name='create-equipment'),
    path('notes/', views.list, name='notes'),
    path('api/v1/client/', views.ClientList.as_view(), name='client'),
    path('api/v1/client/new', views.ClientCreate.as_view(), name='create-client'),
    path('login-end/', views.login),
    path('login/', views.LoginInterfaceView.as_view(), name='login'),
    path('logout', views.LogoutInterfaceView.as_view()),
    path('signup', views.SignupView.as_view(), name='signup'),
]
