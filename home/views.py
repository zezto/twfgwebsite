from django.http import Http404
from .models import Banner, SpanishBanner
from django.shortcuts import render


def index(request):
    words = Banner.objects.all()
    content = ''
    for e in words:
        content += e.content
    context = {'content': content, }
    return render(request, 'home/index.html', context)

def spanish(request):
    text = SpanishBanner.objects.all()
    content = ''
    for e in text:
        content += e.text
    context = {'text': content}
    return render(request, 'home/spanish.html',context)