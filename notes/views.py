from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from .models import Notes


class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = 'notes/register.html'
    success_url = '/smart/login'


class RestrictedView(TemplateView):
    template_name = 'notes/restricted.html'
    raise_exception = True  # Raise exception when no access instead of redirect
    permission_denied_message = "You are not allowed here."

class LogoutInterfaceView(LogoutView):
    template_name = 'notes/logout.html'

class LoginInterfaceView(LoginView):
    template_name = 'notes/login.html'

    # def get_success_url(self):
    #     url = self.get_redirect_url()
    #     if url:
    #         return url
    #     elif self.request.user.is_superuser:
    #         return reverse("admin")
    #     else:
    #         return reverse("profile")


@login_required(login_url='/smart/login/')
def list(request):
    all_notes = Notes.objects.all()
    return render(request, 'notes/notes_list.html', {'notes': all_notes})


def login(request):
    return render(request, 'notes/index.html')
