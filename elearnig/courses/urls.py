from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='courses-home'),
	path('reports/', views.report, name='courses-reports'),
	path(r'^api/courses$', views.course_list),
	path(r'^api/courses/create', views.course_create),
	path(r'^api/courses/(?P<pk>)', views.course_detail),
	path(r'^api/quizes$', views.quiz_list),
	path(r'^api/quizes/create', views.quiz_create),
	path(r'^api/quizes/(?P<pk>)', views.quiz_detail),
]
