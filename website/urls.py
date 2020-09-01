from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home.html', views.home, name='home'),
    path('question.html', views.question, name='question'),
    path('about.html', views.about, name='about'),
    path('service.html', views.service, name='blog'),
    path('contact.html', views.contact, name='contact'),
    
    path('blog.html', views.blog, name='blog'),
    path('blog-details.html', views.blogDetails, name='blog_details'),
]