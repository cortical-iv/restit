"""rest_consume URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
"""
from django.conf.urls import url
from . import views

urlpatterns = [
    #Home page
    url(r'^$', views.index, name = "index"), #views.save_user, name = 'index'),
    #Page to submit a user name
    url(r'^submit/$', views.submit, name = "submit"),
    #Display the users
    url(r'^users/$', views.users, name = "users"),

    ]

