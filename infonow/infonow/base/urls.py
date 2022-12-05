from django.contrib import admin
from django.urls import path
from . import views
from django.views.static import serve
from django.conf.urls import url
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('contactus', views.contactus, name='contactus'),
    path('news', views.news, name='news'),
    path('espn-news', views.espn_news, name='espn_news'),
    path('ign-news', views.ign_news, name='ign_news'),
    path('cnn-news', views.cnn_news, name='cnn_news'),
    path('bbc-news', views.bbc_news, name='bbc_news'),
    path('theverge-news', views.theverge_news, name='theverge_news'),
    path('techcrunch-news', views.techcrunch_news, name='techcrunch_news'),
    # path('football-news', views.football_news, name='football_news'),
    # path('basketball-news', views.basketball_news, name='basketball_news'),
    # path('baseball-news', views.baseball_news, name='baseball_news'),
    # path('cricket-news', views.cricket_news, name='cricket_news'),
    # path('bitcoin-news', views.bitcoin_news, name='bitcoin_news'),
    # path('coronavirus-news', views.coronavirus_news, name='coronavirus_news'),
]
