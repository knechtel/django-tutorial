from django.shortcuts import render
from django.contrib.auth.views import LoginView
from .models import Notes


class LoginInterfaceView(LoginView):
    template_name = 'notes/login.html'

def list(request):
    all_notes = Notes.objects.all()
    return render(request, 'notes/notes_list.html', {'notes': all_notes})


def login(request):
    return render(request, 'notes/index.html')
