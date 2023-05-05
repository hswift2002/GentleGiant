from django.shortcuts import render

from django.http import HttpResponse

from gentle_giant_app.models import Scoreboard
# Create your views here.

def index(request):
    #return HttpResponse ("Hello World")
    my_dict={'insert_me': 'From view.py'}
    return render(request,'gentle_giant_app/index.html', context= my_dict )

def howto(request):
    return render(request,'gentle_giant_app/howto.html')

def game(request):
    return render(request,'gentle_giant_app/game.html')

def tables_view(request):
    scores = Scoreboard.objects.order_by('user_id')
    scoreboard_dict={'scores': scores}
    return render(request, 'gentle_giant_app/index.html', context=scoreboard_dict)

def table(request, pk):
    scores = Scoreboard.objects.get(pk = pk)
    scoreboard_dict = {'scores': scores}
    return render(request, 'gentle_giant_app/table.html', context=scoreboard_dict)

def home(request):
   scoreboard = Scoreboard.objects.all().order_by('-user_score')[:5]
   return render(request, "gentle_giant_app/table.html", {'scoreboard': scoreboard})