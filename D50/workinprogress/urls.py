from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^404/', views.WIP, name='WIP'),
    url(r'^about_NeXT/', views.aboutNEXT, name='aboutNEXT'),
    url(r'^about_this_website/', views.aboutwebsite, name='aboutwebsite'),
    url(r'^logo/', views.logo, name='logo'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^mailinglist/', views.mailinglist, name='mailinglist'),
    url(r'^proposals/', views.proposalDetails, name='proposalDetails'),
    url(r'^downloadform/', views.downloadForm, name='downloadForm'),
    url(r'^neutron_x_ray_matter/', views.neutron_x_ray_matter, name='neutron_x_ray_matter'),
    url(r'^D50/', views.D50, name='D50'),
    url(r'^access_forbidden/', views.access_forbidden, name='access_forbidden'),
    url(r'^access_forbidden_forum/', views.access_forbidden_forum, name='access_forbidden_forum'),
]
