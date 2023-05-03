from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def index(request):
    #return HttpResponse ("Hello World")
    my_dict={'insert_me': 'From view.py'}
    return render(request,'gentle_giant_app/index.html', context= my_dict )