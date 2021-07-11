from django.urls import path, include
from . import views
urlpatterns = [
    path("<int:id", views.index, name="index"),
    path("", views.home, name="home"),
    path('profilelist', views.all_profile, name="profile_list"),
    path('add_profile', views.add_profile, name="add-profile"),
    path('list_profile', views.list_profile, name="list-profile"),
    path('show_profile/<profile_id>', views.show_profile, name='show-profile'),
    path('update_profile/<profile_id>', views.update_profile, name='update-profile'),
    path('delete_profile/<profile_id>', views.delete_profile, name='delete-profile'),

]
 