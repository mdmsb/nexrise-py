from django.shortcuts import render

def index(request):
	return render(request, 'zaid/index-zaid.html')

