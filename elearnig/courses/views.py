from django.shortcuts import render
from django.http import HttpResponse

def home(request):
	return HttpResponse('<h1>Main Courses Site</h1>')

def report(request):
        return HttpResponse('<h1>Reports</h1>')
