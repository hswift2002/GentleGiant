from django import forms 
from django.forms import ModelForm
from .models import Scoreboard

class ScoreForm(ModelForm):
    class Meta:
        model = Scoreboard
        fields = ['user_name', 'user_score']
        labels = {'user_name': 'Initials', 'user_score': 'Score'}