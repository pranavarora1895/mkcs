from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
    path("", views.index, name='home'),
    path("contact", views.contact, name='contact'),
    path("services", views.services, name='services'),
    path("about", views.about, name='about'),
    path("projects", views.projects, name='projects'),
]
