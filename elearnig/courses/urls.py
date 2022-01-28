from django.urls import path, url
from . import views

urlpatterns = [
	path('', views.home, name='courses-home'),
	path('reports/', views.report, name='courses-reports'),
	url(r'^api/tutorials$', views.course_list),
	url(r'^api/tutorials/(?P<pk>[0-9]+)$', views.course_detail),
]
