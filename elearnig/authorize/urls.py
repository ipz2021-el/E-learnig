from django.conf.urls import url
from django.urls import path, include, re_path
from . import views
# from rest_framework import routers
# from authorize.views import UserViewSet

# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)

urlpatterns = [
  path('welcome', views.welcome)
]
