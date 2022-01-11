from django import forms
from django.forms import fields
from django.forms.widgets import SelectDateWidget

from .models import Movie

YEARS= [x for x in range(1940,2023)]

class MovieForm (forms.ModelForm):

     class Meta:
        model = Movie
        fields = ['title', 'content','short_desc', 'model_img', 'director', 'scenariusz', 
        'gatunek', 'kraj', 'data_premiery'
        ]
        widgets = {
            'data_premiery': SelectDateWidget(years=YEARS)
        }


class UpdateMovieForm(forms.ModelForm):
   class Meta:
        model = Movie
        fields = ['title', 'content','short_desc', 'model_img', 'director', 'scenariusz', 
        'gatunek', 'kraj', 'data_premiery'
        ]
        widgets = {
            'data_premiery': SelectDateWidget(years=YEARS)
        }
        
        