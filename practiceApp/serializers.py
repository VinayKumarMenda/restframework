from rest_framework import serializers
from .models import *

class DetailsSerializer(serializers.ModelSerializer):
    class Meta():
        model=Details
        fields='__all__'