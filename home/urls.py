from django.urls import include, path
from . import views

urlpatterns = [
    #homepage
    path('', views.index, name='index'),

]