from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='courses-home'),
	path('reports/', views.report, name='courses-reports'),
	path(r'^api/tutorials$', views.course_list),
	path(r'^api/tutorials/(?P<pk>[0-9]+)$', views.course_detail),
]
