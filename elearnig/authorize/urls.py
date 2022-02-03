from django.urls import path, include
from . import views

urlpatterns = [
    #other paths
    path('totp/create/', views.TOTPCreateView.as_view()),
    path('totp/login/(?P<token>[0-9]{6})/$', views.TOTPVerifyView.as_view()),
    path('static/create/', views.StaticCreateView.as_view()),
    path('static/login/(?P<token>[a-z2-9]{7,8})/$', views.StaticVerifyView.as_view()),
    path('totp/delete/', views.TOTPDeleteView.as_view()),
    path('', views.UserListView.as_view()),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/register/', include('rest_auth.registration.urls')),
]