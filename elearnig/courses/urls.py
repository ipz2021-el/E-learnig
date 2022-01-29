from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='courses-home'),
	path('reports/', views.report, name='courses-reports'),
	path(r'^api/courses$', views.course_list),
	path(r'^api/courses/(?P<pk>[0-9]+)$', views.course_detail),
	path(r'^api/quizes$', views.quiz_list),
	path(r'^api/quizes/(?P<pk>[0-9]+)$', views.quiz_detail),
]
