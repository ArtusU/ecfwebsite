from django.shortcuts import render
from django.core.mail import send_mail



def home(request):
    return render(request, 'home.html', {})


def contact(request):

    if request.method == 'POST':
        name = request.POST['name']
        email2 = request.POST['email']
        intouchmessage = request.POST['message']

        parsedmessage = " Hi. " + name + " from " + email2 + " sent a message: " + intouchmessage

        send_mail(
            'From Get In Touch', 
            parsedmessage, 
            'email2',
            ['email@mail.com'],
        )



        return render(request, 'home.html', {'name': name})
    else:
        return render(request, 'contact.html', {})


def about(request):
    return render(request, 'about.html', {})

def service(request):
    return render(request, 'service.html', {})

def blog(request):
    return render(request, 'blog.html', {})

def blogDetails(request):
    return render(request, 'blog-details.html', {})


def question(request):
    if request.method == 'POST':
        your_name = request.POST['your-name']
        your_phone = request.POST['your-phone']
        your_email = request.POST['your-email']
        your_address = request.POST['your-address']
        your_schedule = request.POST['your-schedule']
        your_nutritionist = request.POST['your-nutritionist']
        your_message = request.POST['your-message']


        message = "Hi" + your_name + ". " + " Our Nutritionist " + your_nutritionist + " will contact you tomorrow between: " + your_schedule + " at " +  your_phone + your_message + " Speak to you soon. "


        send_mail(
            'From Ask Nutritionist', #subject
            message, #message
            'your_email', #from email
            ['email@mail.com'], #to email
        )

        return render(request, 'question.html', {
            'your_name': your_name,
            'your_phone': your_phone,
            'your_email': your_email,
            'your_address': your_address,
            'your_schedule': your_schedule,
            'your_nutritionist': your_nutritionist,
            'your_message': your_message
        })
    else:
        return render(request, 'home.html', {})
