from django.forms import ModelForm
from django.core.exceptions import ValidationError
from accounts.models import Composer, Musictitle , Genre , Country , City , Singer  


class ComposerForm(ModelForm):
    class Meta:
        model = Composer  
        fields = ['first_name', 'last_name', 'date_of_birth', 'date_of_death']


class MusictitleForm(ModelForm):
    class Meta:
        model = Musictitle  
        fields = ['title', 'composer', 'summary', 'isbn', 'genre']

class GenreForm(ModelForm):
    class Meta:
        model = Genre  
        fields = ['name']

class CountryForm(ModelForm):
    class Meta:
        model = Country
        fields = ['name']

class CityForm(ModelForm):
    class Meta:
        model = City  
        fields = ['name']

class SingerForm(ModelForm):
    class Meta:
        model = Singer   
        fields = ['first_name', 'last_name', 'date_of_birth', 'date_of_death']