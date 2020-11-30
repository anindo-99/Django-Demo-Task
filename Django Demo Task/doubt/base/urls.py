from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('lecture', views.lectures, name='lectures'),
    # path('<str:slug>/', views.lecPost, name='lecPost'),
    path('signup', views.handleSignup, name='handleSignup'),
    path('login', views.handleLogin, name='handleLogin'),
    # path('profile', views.profile, name='profile'),
    path('logout', views.handleLogout, name='handleLogout'),
    path('search/', views.search, name='search'),

]
