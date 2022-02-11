import re
from django.shortcuts import render
from django.http import HttpResponse
from courses.models import Course, Quiz
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework.decorators import api_view

from courses.serializers import CourseSerializer, QuizSerializer


def home(request):
	return HttpResponse('<h1>Main Courses Site</h1>')

def report(request):
        return HttpResponse('<h1>Reports</h1>')

@api_view(['GET', 'POST', 'DELETE'])
def courses_list(request):
    courses = Course.objects.all()
    if request.method == 'GET':
        course_serializer = CourseSerializer(courses)
        return JsonResponse(course_serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
def course_detail(request,id):
    course = Course.objects.get(id)
    if request.method == 'GET':
        course_serializer = CourseSerializer(course)
        return JsonResponse(course_serializer.data)
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

@api_view(['POST'])
def course_create(request):
    course_data = JSONParser().parse(request)
    course_serializer = CourseSerializer(data = course_data)
    if course_serializer.is_valid():
        course_serializer.save()
        return JsonResponse(course_serializer.data, status = status.HTTP_201_CREATED)
    return JsonResponse(course_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST', 'DELETE'])
def course_list(request):
    if request.method == 'GET':
        courses = Course.objects.all()
        
        title = request.GET.get('title', None)
        if title is not None:
            courses = courses.filter(title__icontains=title)
        
        courses_serializer = CourseSerializer(courses, many=True)
        return JsonResponse(courses_serializer.data, safe=False)

@api_view(['GET', 'POST', 'DELETE'])
def quizes_list(request):
    quizes = Quiz.objects.all()
    if request.method == 'GET':
        quiz_serializer = QuizSerializer(quizes)
        return JsonResponse(quiz_serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
def quiz_detail(request,id):
    quiz = Quiz.objects.get(id)
    if request.method == 'GET':
        quiz_serializer = QuizSerializer(quiz)
        return JsonResponse(quiz_serializer.data)        
    elif request.method == 'PUT':
        quiz_data = JSONParser().parse(request)
        quiz_serializer = QuizSerializer(quiz,data = quiz_data)
        if quiz_serializer.is_valid():
            quiz_serializer.save()
            return JsonResponse(quiz_serializer.data)
        return JsonResponse(quiz_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        quiz.delete()
        return JsonResponse({'message': 'Quiz deleted succesfully'},status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def quiz_create(request):
    quiz_data = JSONParser().parse(request)
    quiz_serializer = QuizSerializer(data = quiz_data)
    if quiz_serializer.is_valid():
        quiz_serializer.save()
        return JsonResponse(quiz_serializer.data, status = status.HTTP_201_CREATED)
    return JsonResponse(quiz_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST', 'DELETE'])
def quiz_list(request):
    if request.method == 'GET':
        quizes = Quiz.objects.all()
        
        title = request.GET.get('title', None)
        if title is not None:
            quizes = quizes.filter(title__icontains=title)
        
        quizes_serializer = QuizSerializer(quizes, many=True)
        return JsonResponse(quizes_serializer.data, safe=False)
