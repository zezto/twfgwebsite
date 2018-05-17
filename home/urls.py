from django.conf.urls import include, url
from . import views

urlpatterns = [
    #homepage
<<<<<<< HEAD
    path('', views.index, name='index'),
    path('es', views.spanish, name='spanish')
    
=======
    url(r'^', views.index, name='index'),
>>>>>>> 960b8690900046d4e0f7fd35ed32cf8712e10404

]
