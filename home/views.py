from django.http import Http404, HttpResponseRedirect
from .models import Banner, SpanishBanner, contact
from django.shortcuts import render
from .forms import ContactForm
import logging


def index(request):
    words = Banner.objects.all()
    content = ''
    for e in words:
        content += e.content
    form = ContactForm()
    context = {'content': content, 'form': form }
    form = ContactForm()
    return render(request, 'home/index.html', context)

def spanish(request):
    text = SpanishBanner.objects.all()
    content = ''
    for e in text:
        content += e.text
    context = {'text': content}
    return render(request, 'home/spanish.html',context)

def extra(request):
    return render(request,'home/extra.html',)

def mas(request):
    return render(request, 'home/extra_spanish.html')
            
def form(request):
    if request.method == 'GET':
        form = ContactForm()
        context = {'form': form}
        return render(request, 'home/info.html', context)
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            return HttpResponseRedirect('/')
def forma(request):
    if request.method == 'GET':
        form = ContactForm()
        context = {'form': form}
        return render(request, 'home/infospan.html', context)
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            return HttpResponseRedirect('/')

def pros(request):
    if request.method =='POST':
        selected_client = contact.objects.get(pk=request.POST['client'])
        selected_client.worked = True
        selected_client.save()
    cont = contact.objects.all()
    context = {'cont': cont}

    return render (request,'home/prospect.html', context)