
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls')),
]
 
#Configure admin titles
admin.site.site_header = "Vivahavedi Administration page"
admin.site.site_title = "Admin Page"
admin.site.index_title = "Welcome to the Admin area"