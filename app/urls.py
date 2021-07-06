from django.urls import path, include
from . import views
urlpatterns = [
    path("<int:id", views.index, name="index"),
    path("", views.home, name="home"),
    path('profilelist', views.all_profile, name="profile_list")
]
 