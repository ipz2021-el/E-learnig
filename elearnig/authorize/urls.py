from django.conf.urls import url
from django.urls import path, include, re_path
from . import views
from rest_framework import routers
from authorize.views import UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    #other paths
    re_path(r'^totp/create/$', views.TOTPCreateView.as_view(), name='totp-create'),
    re_path(r'^totp/login/(?P<token>[0-9]{6})/$', views.TOTPVerifyView.as_view(), name='totp-login'),
    path(r'', include(router.urls)),
    path(r'auth/', include('rest_auth.urls')),
]