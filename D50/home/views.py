from django.shortcuts import render
from django.contrib.auth.views import logout
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.http import *
from django.template import RequestContext


from django.http import HttpResponseRedirect, HttpResponse


def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')


def index(request):

    return render(request, 'home/index.html')



