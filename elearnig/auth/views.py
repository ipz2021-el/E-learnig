from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from auth.serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from auth.models import User
from auth.serializers import UserSerializer
from elearnig.permissions import IsLoggedInUserOrAdmin, IsAdminUser

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [AllowAny]
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsLoggedInUserOrAdmin]
        elif self.action == 'list' or self.action == 'destroy':
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]