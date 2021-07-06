from django.shortcuts import render
from django.http import HttpResponse
from .models import Profile
# Create your views here.
def all_profile(request):
    profile_list = Profile.objects.all()
    return render(request, 'app/profile_list.html', {'profile_list': profile_list})
 
def index(response, id):
    ls = Profile.objects.get(id=id)
    return render(response, "app/base.html", {})


def home(response):
    return render(response, "app/home.html", {})
