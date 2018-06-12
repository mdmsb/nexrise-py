from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('events/', views.events, name='events'),
    path('contact/', views.contact, name='contact'),
	
	path('ce1/', views.ce1, name='ce1'),
	path('ce2/', views.ce2, name='ce2'),
	path('ce3/', views.ce3, name='ce3'),
	path('ce4/', views.ce4, name='ce4'),
	path('ce5/', views.ce5, name='ce5'),
	path('ce6/', views.ce6, name='ce6'),
]