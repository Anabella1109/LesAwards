from django.shortcuts import render, redirect
from django.http  import HttpResponse,Http404,HttpResponseRedirect

def home(request):
    return render(request,'home.html')

# Create your views here.
