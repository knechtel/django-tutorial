from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.viewsets import ModelViewSet
from notes.serializers import NotesSerialiazers
from .models import Notes
from .serializers import ClientSeriliazers
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view,  permission_classes
from rest_framework.decorators import authentication_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def example_view(request, format=None):
    content = {
        'user': str(request.user),  # `django.contrib.auth.User` instance.
        'auth': str(request.auth),  # None
    }
    print(request.user)
    return Response(content)


class ClientViewSet(ModelViewSet):
    serializer_class = ClientSeriliazers

    def create(self, request, *args, **kwargs):
        equipment = request.equipment
        _serializer = self.serializer_class(data=request.data,
                                            context={'equipment': equipment})
        if _serializer.is_valid():
            _serializer.save()
            return Response(data=_serializer.data, status=status.HTTP_201_CREATED)  # NOQA
        else:
            return Response(data=_serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # NOQA


@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
class NotesList(ListAPIView):
    queryset = Notes.objects.all()
    serializer_class = NotesSerialiazers


@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = 'notes/register.html'
    success_url = '/smart/login'


@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
class NotesCreate(CreateAPIView):
    serializer_class = NotesSerialiazers

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user_name = serializer.get('user')
            project_name = serializer.get('project_name')
            user = Users.objects.get(user=user_name)
            project = User.objects.get(pk=id)
            project.user = user
            project.user.save()
            return Response(ProjectSerializer(project).data, status=status.HTTP_201_CREATED)
        else:
            return HttpResponse("Incorrect Credentials")


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


@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def list(request):
    all_notes = Notes.objects.all()
    return render(request, 'notes/notes_list.html', {'notes': all_notes})


def login(request):
    return render(request, 'notes/index.html')
