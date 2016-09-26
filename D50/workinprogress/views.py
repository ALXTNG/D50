from django.shortcuts import render
from django.http import HttpResponse



def WIP(request):
    return render(request, 'workinprogress/WIP.html')

def aboutNEXT(request):
    return render(request, 'workinprogress/aboutNEXT.html')
    
def logo(request):
    return render(request, 'workinprogress/logo.html')
    
def contact(request):
    return render(request, 'workinprogress/contact.html')
    
def mailinglist(request):
    return render(request, 'workinprogress/mailinglist.html')

#~ def index(request):
    #~ return HttpResponse("Hello, world. You're at the polls index.")
