from django.shortcuts import render
from django.contrib.auth.views import logout
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.http import *
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse

from .models import  Post


def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')
    
    
def index(request):
    post_list = Post.objects.order_by('-pub_date')[:]
    context = {'post_list': post_list}
    return render(request, 'home/index.html', context)



