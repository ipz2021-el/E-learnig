from rest_framework import permissions
from rest_framework import views
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from authorize.serializers import UserSerializer
from django.contrib.auth.models import User

from django.shortcuts import render
from django_otp.plugins.otp_totp.models import TOTPDevice
from django_otp import devices_for_user
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from authorize.models import elearningUser
from authorize.serializers import UserSerializer
from elearnig.permissions import IsLoggedInUserOrAdmin, IsAdminUser
from rest_framework import status
from django_otp import devices_for_user
from django_otp.plugins.otp_totp.models import TOTPDevice

class UserViewSet(viewsets.ModelViewSet):
    queryset = elearningUser.objects.all()
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

 

def get_user_totp_device(self, user, confirmed=None):
    devices = devices_for_user(user, confirmed=confirmed)
    for device in devices:
        if isinstance(device, TOTPDevice):
            return device

class TOTPCreateView(views.APIView):
    """
    Use this endpoint to set up a new TOTP device
    """
    permission_classes = [permissions.IsAuthenticated]    
    def get(self, request, format=None):
        user = request.user
        device = get_user_totp_device(self, user)
        if not device:
            device = user.totpdevice_set.create(confirmed=False)
        url = device.config_url
        return Response(url, status=status.HTTP_201_CREATED)

class TOTPVerifyView(views.APIView):
    """
    Use this endpoint to verify/enable a TOTP device
    """
    permission_classes = [permissions.IsAuthenticated]    
    def post(self, request, token, format=None):
        user = request.user
        device = get_user_totp_device(self, user)
        if not device:
            return Response(dict(
           errors=['This user has not setup two factor authentication']),
                status=status.HTTP_400_BAD_REQUEST
            )        
        if not device == None and device.verify_token(token):
            if not device.confirmed:
                device.confirmed = True
                device.save()
                user.is_two_factor_enabled=True
                user.save()
            return Response(dict(token=user.token),   status=status.HTTP_200_OK)    
        return Response(dict(errors=dict(token=['Invalid TOTP Token'])),
                        status=status.HTTP_400_BAD_REQUEST)