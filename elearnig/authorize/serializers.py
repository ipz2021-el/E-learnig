from rest_framework import serializers
from . import models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.eustomUser
        fields = ('username', 'first_name', 'last_name', 'index_number' )