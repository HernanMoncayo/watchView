from django.contrib import admin
from django.urls import path, include  # add this
from apps.home import views  # add


urlpatterns = [
    path('admin/', admin.site.urls), 
    path("", include("apps.authentication.urls")),

    path("", include("apps.home.urls")),


]
