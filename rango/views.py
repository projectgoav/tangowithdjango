from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

#Basic Index
def index(request):

	#Adds data to the variables in the index.html template
	context_dic = { 'boldmessage' : "I am bold font from the context"}

	return render(request, 'rango/index.html', context_dic)

#Basic About
def about(request):

	#Adds the about Info to the page
	context_dic = { 'Page_Content' : "This tutorial has been put together by Ewan McCartney (2025797M)"}

	return render(request, 'rango/about.html', context_dic)