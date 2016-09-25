from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^404/', views.WIP, name='WIP'),
    url(r'^about/', views.aboutNEXT, name='aboutNEXT'),
    url(r'^logo/', views.logo, name='logo'),
]
