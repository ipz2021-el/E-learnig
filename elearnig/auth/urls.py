from django.conf.urls import url
from django.urls import path, include, url
from . import views
from rest_framework import routers
from auth.views import UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    #other paths
    path(r'', include(router.urls)),
    path(r'auth/', include('rest_auth.urls')),
]