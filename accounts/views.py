from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.forms.models import model_to_dict
from django.http import HttpResponse, HttpResponseRedirect
from accounts.models import Musictitle, Composer, Genre, Country, City, Singer
from django.urls import reverse
from accounts.forms import ComposerForm, MusictitleForm, GenreForm, CountryForm, CityForm, SingerForm

def indexView(request):
	return render(request, 'indexView.html')
@login_required
def dashboardView(request):
	return render(request, 'dashboard.html')

def registerView(request):
	if request.method == "POST":
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('login.url')
	else:
		form = UserCreationForm()
	return render(request,'register.html',{'form':form})

def index(request):
    # get all info here including authors, books, and genres
    num_musictitles = Musictitle.objects.all().count()
    num_composers = Composer.objects.all().count()
    num_genres = Genre.objects.all().count()
    context = {
        'num_musictitles': num_musictitles,
        'num_composers': num_composers,
        'num_genres' : num_genres,
    }
    return render(request, 'index.html', context=context)

def list_composers(request):
    # get all authors and add to context dictionary
    composers = Composer.objects.all()
    context = {
        'composers': composers,
    }
    # process the template and pass the context
    return render(request, 'composers.html', context=context)

def list_genres(request):
    # get all authors and add to context dictionary
    genres = Genre.objects.all()
    context = {
        'genres': genres,
    }
    # process the template and pass the context
    return render(request, 'genres.html', context=context)

def list_musictitles(request):
    # get all authors and add to context dictionary
    musictitles = Musictitle.objects.all()
    context = {
        'musictitles': musictitles,
    }
    # process the template and pass the context
    return render(request, 'musictitles.html', context=context)

def list_countrys(request):
    # get all authors and add to context dictionary
    countrys = Country.objects.all()
    context = {
        'countrys': countrys,
    }
    # process the template and pass the context
    return render(request, 'countrys.html', context=context) 

def list_citys(request):
    # get all authors and add to context dictionary
    citys = City.objects.all()
    context = {
        'citys': citys,
    }
    # process the template and pass the context
    return render(request, 'citys.html', context=context) 

def list_singers(request):
    # get all authors and add to context dictionary
    singers = Singer.objects.all()
    context = {
        'singers': singers,
    }
    # process the template and pass the context
    return render(request, 'singers.html', context=context)          

def add_composer(request):
    if request.method == 'POST':
        form = ComposerForm(request.POST)
        if form.is_valid():
            form.save()  # directly save the form
            return HttpResponseRedirect(reverse('composers'))
    else:
        form = ComposerForm()

    context = {
        'form': form
    }
    return render(request, 'composer_form.html', context=context)


def edit_composer(request, composer_id):
    if request.method == 'POST':
        composer = Composer.objects.get(pk=composer_id)
        form = ComposerForm(request.POST, instance=composer)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('composers'))
    else:
        composer = Composer.objects.get(pk=composer_id)
        fields = model_to_dict(composer)
        form = ComposerForm(initial=fields, instance=composer)
    context = {
        'form': form,
        'type': 'edit',
    }
    return render(request, 'composer_form.html', context=context)

def delete_composer(request, composer_id):
    composer = Composer.objects.get(pk=composer_id)
    if request.method == 'POST':
        composer.delete()
        return HttpResponseRedirect(reverse('composers'))
    context = {
        'composer': composer
    }
    return render(request, 'composer_delete_form.html', context=context)


def add_musictitle(request):
    if request.method == 'POST':
        form = MusictitleForm(request.POST)
        if form.is_valid():
            form.save()  # directly save the form
            return HttpResponseRedirect(reverse('musictitles'))
    else:
        form = MusictitleForm()

    context = {
        'form': form
    }
    return render(request, 'musictitle_form.html', context=context)


def edit_musictitle(request, musictitle_id):
    if request.method == 'POST':
        musictitle = Musictitle.objects.get(pk=musictitle_id)
        form = MusictitleForm(request.POST, instance=musictitle)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('musictitles'))
    else:
        musictitle = Musictitle.objects.get(pk=musictitle_id)
        fields = model_to_dict(musictitle)
        form = MusictitleForm(initial=fields, instance=musictitle)
    context = {
        'form': form,
        'type': 'edit',
    }
    return render(request, 'musictitle_form.html', context=context)

def delete_musictitle(request, musictitle_id):
    musictitle = Musictitle.objects.get(pk=musictitle_id)
    if request.method == 'POST':
        musictitle.delete()
        return HttpResponseRedirect(reverse('musictitles'))
    context = {
        'musictitle': musictitle
    }
    return render(request, 'musictitle_delete_form.html', context=context)

def add_genre(request):
    if request.method == 'POST':
        form = GenreForm(request.POST)
        if form.is_valid():
            form.save()  # directly save the form
            return HttpResponseRedirect(reverse('genres'))
    else:
        form = GenreForm()

    context = {
        'form': form
    }
    return render(request, 'genre_form.html', context=context)


def edit_genre(request, genre_id):
    if request.method == 'POST':
       genre = Genre.objects.get(pk=genre_id)
       form = GenreForm(request.POST, instance=genre)
       if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('genres'))
    else:
        genre = Genre.objects.get(pk=genre_id)
        fields = model_to_dict(genre)
        form = GenreForm(initial=fields, instance=genre)
    context = {
        'form': form,
        'type': 'edit',
    }
    return render(request, 'genre_form.html', context=context)

def delete_genre(request, genre_id):
    genre = Genre.objects.get(pk=genre_id)
    if request.method == 'POST':
        genre.delete()
        return HttpResponseRedirect(reverse('genres'))
    context = {
        'genre': genre
    }  
    return render(request, 'genre_delete_form.html', context=context)

def add_country(request):
    if request.method == 'POST':
        form = CountryForm(request.POST)
        if form.is_valid():
            form.save()  # directly save the form
            return HttpResponseRedirect(reverse('countrys'))
    else:
        form = CountryForm()

    context = {
        'form': form
    }
    return render(request, 'country_form.html', context=context)

def edit_country(request, country_id):
    if request.method == 'POST':
       country = Country.objects.get(pk=country_id)
       form = CountryForm(request.POST, instance=country)
       if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('countrys'))
    else:
        country = Country.objects.get(pk=country_id)
        fields = model_to_dict(country)
        form = CountryForm(initial=fields, instance=country)
    context = {
        'form': form,
        'type': 'edit',
    }
    return render(request, 'country_form.html', context=context)

def delete_country(request, country_id):
    country = Country.objects.get(pk=country_id)
    if request.method == 'POST':
        country.delete()
        return HttpResponseRedirect(reverse('countrys'))
    context = {
        'country': country
    }  
    return render(request, 'country_delete_form.html', context=context)

def add_city(request):
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            form.save()  # directly save the form
            return HttpResponseRedirect(reverse('citys'))
    else:
        form = CityForm()

    context = {
        'form': form
    }
    return render(request, 'city_form.html', context=context)

def edit_city(request, city_id):
    if request.method == 'POST':
       city = City.objects.get(pk=citry_id)
       form = CityForm(request.POST, instance=country)
       if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('citys'))
    else:
        city = City.objects.get(pk=city_id)
        fields = model_to_dict(city)
        form = CityForm(initial=fields, instance=city)
    context = {
        'form': form,
        'type': 'edit',
    }
    return render(request, 'city_form.html', context=context)

def delete_city(request, city_id):
    city = City.objects.get(pk=city_id)
    if request.method == 'POST':
        city.delete()
        return HttpResponseRedirect(reverse('citys'))
    context = {
        'city': city
    }  
    return render(request, 'city_delete_form.html', context=context)      

def add_singer(request):
    if request.method == 'POST':
        form = SingerForm(request.POST)
        if form.is_valid():
            form.save()  # directly save the form
            return HttpResponseRedirect(reverse('singers'))
    else:
        form = SingerForm()

    context = {
        'form': form
    }
    return render(request, 'singer_form.html', context=context)


def edit_singer(request, singer_id):
    if request.method == 'POST':
        singer = Singer.objects.get(pk=singer_id)
        form = SingerForm(request.POST, instance=singer)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('singers'))
    else:
        singer = Singer.objects.get(pk=singer_id)
        fields = model_to_dict(singer)
        form = SingerForm(initial=fields, instance=singer)
    context = {
        'form': form,
        'type': 'edit',
    }
    return render(request, 'singer_form.html', context=context)

def delete_singer(request, singer_id):
    singer = Singer.objects.get(pk=singer_id)
    if request.method == 'POST':
        singer.delete()
        return HttpResponseRedirect(reverse('singers'))
    context = {
        'singer': singer
    }
    return render(request, 'singer_delete_form.html', context=context)          