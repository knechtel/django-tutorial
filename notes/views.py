from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from .models import Notes


class LogoutInterfaceView(LogoutView):
    template_name = 'notes/logout.html'

class LoginInterfaceView(LoginView):
    template_name = 'notes/login.html'


@login_required
def list(request):
    all_notes = Notes.objects.all()
    return render(request, 'notes/notes_list.html', {'notes': all_notes})


def login(request):
    return render(request, 'notes/index.html')
