import re
from django.shortcuts import render
from django.http import HttpResponse
from flask_login import login_required

from courses.models import Course
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework.decorators import api_view

from courses.serializers import CourseSerializer


def home(request):
	return HttpResponse('<h1>Main Courses Site</h1>')

def report(request):
        return HttpResponse('<h1>Reports</h1>')

@login_required
@api_view(['GET', 'POST', 'DELETE'])
def courses_list(request):
    pass

@login_required
@api_view(['GET', 'POST', 'DELETE'])
def course_detail(request,id):
    course = Course.objects.get(id)
    if request.method == 'GET':
        course_serializer = CourseSerializer(course)
        return JsonResponse(course_serializer.data)
    elif request.method == 'POST':
        course_data = JSONParser().parse(request)
        course_serializer = CourseSerializer(data = course_data)
        if course_serializer.is_valid():
            course_serializer.save()
            return JsonResponse(course_serializer.data, status = status.HTTP_201_CREATED)
        return JsonResponse(course_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PUT':
        course_data = JSONParser().parse(request)
        course_serializer = CourseSerializer(course,data = course_data)
        if course_serializer.is_valid():
            course_serializer.save()
            return JsonResponse(course_serializer.data)
        return JsonResponse(course_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        course.delete()
        return JsonResponse({'message': 'Course deleted succesfully'},status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST', 'DELETE'])
def course_list(request):
    if request.method == 'GET':
        courses = Course.objects.all()
        
        title = request.GET.get('title', None)
        if title is not None:
            courses = courses.filter(title__icontains=title)
        
        courses_serializer = CourseSerializer(courses, many=True)
        return JsonResponse(courses_serializer.data, safe=False)
