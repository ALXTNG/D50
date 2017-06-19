from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^404/', views.WIP, name='WIP'),
    url(r'^about/', views.aboutNEXT, name='aboutNEXT'),
    url(r'^logo/', views.logo, name='logo'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^mailinglist/', views.mailinglist, name='mailinglist'),
    url(r'^proposals/', views.proposalDetails, name='proposalDetails'),
    url(r'^downloadform/', views.downloadForm, name='downloadForm'),
    url(r'^proposalsubmission/', views.proposalSubmission, name='proposalSubmission'),
    url(r'^neutron_x_ray_matter/', views.neutron_x_ray_matter, name='neutron_x_ray_matter'),
]
