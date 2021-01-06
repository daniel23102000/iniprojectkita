from django.contrib import admin
from .models import Composer, Musictitle, Genre , Country , City , Singer


admin.site.register(Composer)
admin.site.register(Musictitle)
admin.site.register(Genre)
admin.site.register(Country)
admin.site.register(City)
admin.site.register(Singer)