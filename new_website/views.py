from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views.generic import View
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def home(request):
    return render(request,'prof/home.html')

@login_required
def profile_page(request):
    user = request.user
    return render(request, 'registration/profile.html', {'profile_user': user})