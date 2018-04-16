from django.conf.urls import include, url
from . import views

urlpatterns = [
    #homepage
    url(r'^', views.index, name='index'),

]
