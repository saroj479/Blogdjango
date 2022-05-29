from rest_framework.serializers import ModelSerializer
from .models import Noteregister


class NoteregisterSerializer(ModelSerializer):
    class Meta:
        model=Noteregister
        fields='__all__'


