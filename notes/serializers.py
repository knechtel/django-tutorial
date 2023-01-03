from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from notes.models import Notes, Client, Equipment
from django.db import models


class NotesDto(models.Model):
    title = ''
    text = ''
    user = None

class NotesSerialiazers(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        return data


class ClientSeriliazers(ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class EquipmentSeriliazers(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = '__all__'
