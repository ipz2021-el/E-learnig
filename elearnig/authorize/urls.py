from django.urls import path, include
from . import views
from rest_framework import routers
from authorize.views import UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    #other paths
    path('totp/create/$', views.TOTPCreateView.as_view(), name='totp-create'),
    path('totp/login/(?P<token>[0-9]{6})/$', views.TOTPVerifyView.as_view(), name='totp-login'),
    path('', include(router.urls)),
    path('rest-auth/', include('rest_auth.urls')),

]