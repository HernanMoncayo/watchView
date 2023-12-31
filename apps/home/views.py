from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import CreateView, DeleteView, UpdateView, ListView, DetailView
from django.template import loader
from django.urls import reverse
from .models import Plataform, Director, Movie
from .imdb_api import get_movie_data

@login_required(login_url="/login/")
def index(request):
  context = {'segment': 'index'}
  html_template = loader.get_template('home/index.html')
  return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def pages(request):
  context = {}

  try:
    load_template = request.path.split('/')[-1]

    if load_template == 'admin':
        return HttpResponseRedirect(reverse('admin:index'))

    context['segment'] = load_template

    if load_template == 'movies':
      movies = Movie.objects.all()
      context['movies'] = movies

      movie_data = get_movie_data("game")
      context['movie_data'] = movie_data

    elif load_template == 'directors':
      directors = Director.objects.all()
      context['directors'] = directors

    elif load_template == 'plataforms':
      plataforms = Plataform.objects.all()
      context['plataforms'] = plataforms
    
    elif load_template == 'movies-details':
      movie = Movie.objects.get(pk=request.GET.get('id'))
      context['movie'] = movie

    html_template = loader.get_template('home/' + load_template + '.html')
    return HttpResponse(html_template.render(context, request))


  except template.TemplateDoesNotExist:
    html_template = loader.get_template('home/page-404.html')
    return HttpResponse(html_template.render(context, request))

  except:
    html_template = loader.get_template('home/page-500.html')
    return HttpResponse(html_template.render(context, request))

