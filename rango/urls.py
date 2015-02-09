from django.conf.urls import patterns, url
from rango import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^about/', views.about, name = 'about'),
        url(r'^add_category/$', views.add_category, name='add_category'),
        url(r'^category/(?P<category_name_slug>[\w\-]+)/add_page/$', views.add_page, name='add_page'),
        url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.category, name='category'),
        url(r'^restricted/', views.restricted, name='restricted'),

        #Used to track the URL of the Page for views
        url(r'^goto/$', views.track_url, name='goto'),

        #NO LONGER NEEDED FROM CHAPTER 12:
        #url(r'^register/$', views.register, name='registration_register'),
        #url(r'^login/$', views.user_login, name='auth_login'),
        #url(r'^logout/$', views.user_logout, name='auth_logout'),

                #Removed from Chapter 16 ->
        #url(r'^search/', views.search, name='search'),
        
        )