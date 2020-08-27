from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home.html', views.home, name='home'),
    path('contact.html', views.contact, name='contact'),
    path('blog.html', views.blog, name='blog'),
]