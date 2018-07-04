from django.urls import include
from django.conf.urls import url
from . import views
urlpatterns = [
    
    url(r'^$', views.details),
    url(r'IOT/$', views.iot),
    url(r'Ethical Hacking/$', views.eh),
    url(r'Augmented Reality/$', views.ar),
    url(r'Machine Learning/$', views.ml),
]
