from django.shortcuts import render


def home(request):
    context = {
        'a' : 'Homepage',
        'q' : 'Hey! we welcome you here'
    }

    return render(request, 'list/home.html', context )


def contact(request):
    context = {
        'a' : 'Contactpage',
        'q' : 'Hello! In case of any query feel free to connect with us'
    }
    return render(request, 'list/home.html', context)

