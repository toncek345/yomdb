from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse
from django.utils import timezone

from django.http import HttpResponse, \
    HttpResponseNotFound, \
    HttpResponseRedirect

from .models import Movie, Actor, Genre

from yomdb.settings import OMDB_KEY

import json
import requests


def searchMovies(url):
    # returns parsed json of search
    asdf = url.replace(" ", "+")
    r = requests.get("http://www.omdbapi.com/?apikey={0}&s={1}".format(
        OMDB_KEY, asdf))
    return json.loads(r.content)


def getData(movieName):
    # returnes parsed json for particular movie
    n = movieName.replace(" ", "+")
    n = n.replace(':', '%3A')
    r = requests.get("http://www.omdbapi.com/?apikey={0}&t={1}".format(
        OMDB_KEY, n))
    return json.loads(r.content)


def index(request):
    return render(request, 'mdb/index.djhtml')


def showMovies(request):
    # returnes the movies from search
    if request.method != "POST":
        return HttpResponseNotFound("wrong url, wrong request")

    movieStr = request.POST["title"]
    data = searchMovies(movieStr)
    if not data["Response"]:
        return HttpResponse(request, "api went wrong")

    if data["Response"] != "True":
        context = {'response': data["Response"], 'data': data["Error"]}
    else:
        context = {
            'response': data["Response"],
            'data': data["Search"],
        }
    return render(request, 'mdb/show.djhtml', context)


def save(request):
    # save movie to db and update actors and genres if not there
    # redirects to watchlist
    if request.method != "POST":
        return HttpResponseNotFound("wrong url, wrong request")

    data = getData(request.POST["title"])
    if not data["Response"]:
        return HttpResponse(request, "api went wrong")

    try:
        m = Movie.objects.get(title=data["Title"])
        return HttpResponseRedirect(reverse('mdb:watchlist'))
    except ObjectDoesNotExist:
        m = Movie(title=data["Title"], time_added=timezone.now())
        m.save()

        actors = data["Actors"].split(', ')
        for a in actors:
            obj, created = Actor.objects.get_or_create(name=a)
            if created:
                obj.save()
            m.actors.add(obj)

        genres = data["Genre"].split(', ')
        for g in genres:
            obj, created = Genre.objects.get_or_create(genre_text=g)
            if created:
                obj.save()
            m.genres.add(obj)
        return HttpResponseRedirect(reverse('mdb:watchlist'))


def showWatchlist(request):
    # returnes all movies in watchlist
    return render(request, 'mdb/movies.djhtml', {
        'movies': Movie.objects.all(),
        'genre': Genre.objects.all()
    })


def update(request, pk):
    # watched/unwatched
    m = Movie.objects.get(id=pk)
    if m.watched:
        m.watched = False
        m.save()
    else:
        m.watched = True
        m.save()
    return HttpResponseRedirect(reverse('mdb:watchlist'))


def delete(request, pk):
    # delete movie from db
    m = Movie.objects.get(id=pk)
    m.delete()
    return HttpResponseRedirect(reverse('mdb:watchlist'))


def filters(request):
    if request.method != "POST":
        return HttpResponseNotFound("wrong url, wrong request")

    m = Movie.objects.all()
    if request.POST["watched"] != "":
        m = m.filter(watched=strToBool(request.POST["watched"]))

    if request.POST["actor"] != "":
        m = m.filter(actors__name__icontains=request.POST["actor"])

    if request.POST["genre"] != "":
        m = m.filter(genres__genre_text__exact=request.POST["genre"])

    return render(request, 'mdb/movies.djhtml', {
        'movies': m,
        'genres': Genre.objects.all()
    })


def strToBool(string):
    if string == "True":
        return True
    else:
        return False
