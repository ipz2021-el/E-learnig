from rest_framework import serializers
from . import models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.elearningUser
        fields = ('username', 'first_name', 'last_name', 'index_number' )