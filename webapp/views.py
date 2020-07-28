from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')
def blog(request):
    return render(request,'blog.html')
def contact(request):
    mapbox_access_token = 'pk.my_mapbox_access_token'
    return render(request,'contact.html',{ 'mapbox_access_token': mapbox_access_token })
def destination(request):
    return render(request,'destination.html')

