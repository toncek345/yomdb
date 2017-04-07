from django.conf.urls import url
from . import views


app_name = 'mdb'

urlpatterns = [
    # search and index
    url(r'^$', views.index, name='index'),

    # returnes movies from search
    url(r'^load/$', views.showMovies, name='showMovies'),

    # urls for navigating through watchlist db
    url(r'^watchlist/save/$', views.save, name='save'),
    url(r'^watchlist/$', views.showWatchlist, name='watchlist'),
    url(r'^watchlist/filter/$', views.filters, name='filter'),
    url(r'^watchlist/update/(?P<pk>[0-9]+)/$', views.update, name='update'),
    url(r'^watchlist/delete/(?P<pk>[0-9]+)/$', views.delete, name='delete'),
]
