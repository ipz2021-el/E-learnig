from django.urls import path, include
from . import views

urlpatterns = [
    #other paths
    path('', views.UserListView.as_view()),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/register/', include('rest_auth.registration.urls')),
    path('mfa/',include('trench.urls')),
    path('mfa/',include('trench.urls.jwt'))
]