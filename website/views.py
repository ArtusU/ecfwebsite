from django.shortcuts import render
from django.core.mail import send_mail



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


def blog(request):
    return render(request, 'blog.html', {})
