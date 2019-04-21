from django.shortcuts import render
from other.models import Banner


# Create your views here.
def index(request):
    banner = Banner.objects.all()
    return render(request, 'index.html', {'banner': banner})


def harm(request):
    return render(request, 'harm.html')


def governance(request):
    return render(request, 'governance.html')


def about(request):
    return render(request, 'about.html')


def handler_404(request):
    ret = render(request, '404.html')
    ret.status_code = 404
    return ret


def handler_500(request):
    ret = render(request, '500.html')
    ret.status_code = 500
    return ret
