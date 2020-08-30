from django.urls import path
from . import views

from .views import NewBlogView, NewBlogDetailView

urlpatterns = [
    path('', views.home, name='home'),
    path('home.html', views.home, name='home'),
    path('about.html', views.about, name='about'),
    path('service.html', views.service, name='blog'),
    path('contact.html', views.contact, name='contact'),
    
    path('blog.html', views.blog, name='blog'),
    path('blog-details.html', views.blogDetails, name='blog_details'),

    #path('blogpost', BlogView.as_view(), name='blogpost'),
    
    
    path('newblog', NewBlogView.as_view(), name='newblog'),
    path('newblog/<int:pk>', NewBlogDetailView.as_view(), name='newblogdetail'),

]