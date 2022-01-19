from django.urls import path, include
from . import views
from rest_framework import routers

urlpatterns = [
    #other paths
    path('totp/create/$', views.TOTPCreateView.as_view(), name='totp-create'),
    path('totp/login/(?P<token>[0-9]{6})/$', views.TOTPVerifyView.as_view(), name='totp-login'),
    path('', views.UserListView.as_view()),
    path('rest-auth/', include('rest_auth.urls')),
]