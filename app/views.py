from django.forms.forms import Form
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import Profile
from .forms import ProfileForm
# Create your views here.

def delete_profile(request, profile_id):
    profile = Profile.objects.get(pk=profile_id)
    profile.delete()
    return redirect('list-profile')

def update_profile(request, profile_id):
    profile = Profile.objects.get(pk=profile_id)
    form = ProfileForm(request.POST or None, instance=profile)
    if form.is_valid():
        form.save()
        return redirect('list-profile')
    return render(request, 'app/update_profile.html', {'profile': profile, 'form': form})
 


def show_profile(request, profile_id):
    profile = Profile.objects.get(pk=profile_id)
    return render(request, 'app/show_profile.html', {'profile': profile})

def list_profile(request):
    profile_list = Profile.objects.all().order_by('id')
    return render(request, 'app/profile.html', {'profile_list': profile_list})
 

def add_profile(request):
    submitted = False
    if request.method == "POST":
        form = ProfileForm(request.POST)
        form.save()
        return HttpResponseRedirect('/add_profile?submitted=True')
    else:
        form = ProfileForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'app/add_profile.html', {'form':form, 'submitted':submitted})


def all_profile(request):
    profile_list = Profile.objects.all()
    return render(request, 'app/profile_list.html', {'profile_list': profile_list})
 
def index(response, id):
    ls = Profile.objects.get(id=id)
    return render(response, "app/base.html", {})


def home(response):
    return render(response, "app/home.html", {})
