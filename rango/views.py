from django.shortcuts import render
from rango.models import Category, Page

# Create your views here.
from django.http import HttpResponse

#Basic Index
def index(request):
    #Queries for all categories by likes and then orders and shows top 5
    category_list = Category.objects.order_by('-likes')[:5]
    page_list = Page.objects.order_by('-views')[:5]
    context_dict = {'categories': category_list,
                    'pages': page_list,
                    }

    # Render the response and send it back!
    return render(request, 'rango/index.html', context_dict)

#Basic About
def about(request):

	#Adds the about Info to the page
	context_dic = { 'Page_Content' : "This tutorial has been put together by Ewan McCartney (2025797M)"}

	return render(request, 'rango/about.html', context_dic)

def category(request, category_name_slug):

    # Create a context dictionary which we can pass to template
    context_dict = {}

    try:
        category = Category.objects.get(slug=category_name_slug)
        context_dict['category_name'] = category.name
        pages = Page.objects.filter(category=category)
        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        # Don't do anything - template displays message
        pass

    return render(request, 'rango/category.html', context_dict)
