from rest_framework import serializers
from notes.models import Notes


class NotesSerialiazers(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = ('title', 'text')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        return data
