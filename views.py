from django.shortcuts import render

def index(request):
	return render(request, 'nexrise/index-nexrise.html')

def about(request):
	return render(request, 'nexrise/about-us.html')

def events(request):
	return render(request, 'nexrise/events.html')

def contact(request):
	return render(request, 'nexrise/contact.html')



def ce1(request):
	return render(request, 'nexrise/events/ce1.html')

def ce2(request):
	return render(request, 'nexrise/events/ce2.html')

def ce3(request):
	return render(request, 'nexrise/events/ce3.html')

def ce4(request):
	return render(request, 'nexrise/events/ce4.html')

def ce5(request):
	return render(request, 'nexrise/events/ce5.html')

def ce6(request):
	return render(request, 'nexrise/events/ce6.html')

