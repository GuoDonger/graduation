from django.shortcuts import render
from other.models import Banner


# Create your views here.
def index(request):
    banner = Banner.objects.all()
    return render(request, 'index.html', {'banner': banner})


def knowledge(request):
    return render(request, 'knowledge.html')


def contact(request):
    return render(request, 'contact.html')


# def data(request):
#     return render(request, 'data.html')
