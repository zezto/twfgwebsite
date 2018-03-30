from django.http import Http404
from .models import Banner
from django.shortcuts import render


def index(request):
    words = Banner.objects.all()
    content = ''
    for e in words:
        content += e.content
    context = {'content': content, }
    return render(request, 'home/index.html', context)
