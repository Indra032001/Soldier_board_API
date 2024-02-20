from rest_framework import serializers
from .models import SBoard


class BoardSerializers(serializers.ModelSerializer):
    class Meta:
        model = SBoard
        fields = '__all__'
