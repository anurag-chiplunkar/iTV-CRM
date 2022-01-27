from django.shortcuts import render,redirect

## Defining the home page
def home(request):
	return render(request,'home/home.html')