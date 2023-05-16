from django.urls import path
from . import views
from pfaApp import api

urlpatterns = [
    path("",views.ViewPage, name="index"),
    path("register/", views.UserReg, name="register"),
    path("loginpage/", views.LoginPage, name="loginpage"),
    path("login/", views.Login, name="login"),
    path("read/", views.readmore, name="readmore"),

    #Urls fot BPM and graphe
    path("bpm/", views.BPM1, name="bpm"),
    path("graphe/", views.BPM2, name="graphe"),

    #URLs for pression and graphe
    path("pression/",views.PRESSION1, name="pression"),
    path("pgraphe/", views.PRESSION2, name="pgraphe"),

    #URLs for temperature and graphe
    path('temperature/', views.Temp1, name='temperature'),
    path('tgraphe', views.Temp2, name='tgraphe'),


    path('api/list', api.Dlist, name='BPMList'),
    path('api/post', api.BPMviews.as_view(), name='BPM_post'),

    path('api/listp', api.Plist, name='PRESSIONList'),
    path('api/post1', api.PRESSIONviews.as_view(), name='PRESSION_post'),

    path('api/listt', api.Tlist, name='TEMPERATUREList'),
    path('api/post2', api.Tempviews.as_view(), name='temp_post'),


    path('csv', views.exp_csv, name='exp-csv'),
    path('csv1', views.exp_csv1, name='pression-csv'),
    path('csv2', views.exp_csv2, name='temperature-csv')
]
