from rest_framework import serializers
from . import models

class CourseSerializer(serializers.ModelSerializer):
    model = models.Course
    fields = ['owner','subject','title','overview','modules',]

class QuizSerializer(serializers.ModelSerializer):
    model = models.Quiz
    fields = ['owner''title','questions']