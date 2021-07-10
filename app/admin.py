from django.contrib import admin
from .models import Profile

# Register your models here.
#admin.site.register(Profile)
#Another way to register model and increase data details
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Age', 'Place')
    ordering = ('Name',)
    search_fields = ('Name', 'Age')