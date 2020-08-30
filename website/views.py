from django.shortcuts import render
from django.core.mail import send_mail
from django.views.generic import ListView, DetailView
from website.models import Post



def home(request):
    return render(request, 'home.html', {})


def contact(request):
    '''
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        send_mail(
            name,
            email,
            message,
            ['admin@edinburghcommunityfood.org.uk'],
        )

        return render(request, 'home.html', {'name': name})
    else:
        '''
    return render(request, 'contact.html', {})


def about(request):
    return render(request, 'about.html', {})

def service(request):
    return render(request, 'service.html', {})

def blog(request):
    return render(request, 'blog.html', {})

def blogDetails(request):
    return render(request, 'blog-details.html', {})


#class Blog(ListView):
    model = Post
    template_name = 'blog.html'


class NewBlogView(ListView):
    model = Post
    template_name = 'blog2.html'


class NewBlogDetailView(DetailView):
    model = Post
    template_name = 'newblog-details.html'