from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

#Basic Index
def index(request):
	return HttpResponse("Rango says hello! | <a href='/rango/about'>About Me!</a>")

#Basic About
def about(request):
	return HttpResponse("This tutorial has been put together by Ewan McCartney (2025797) | <a href='/rango/'>Return</a>")