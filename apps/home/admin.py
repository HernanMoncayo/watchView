# -*- encoding: utf-8 -*-
from django.contrib import admin

# Register your models here.

from .models import Plataform, Director, Movie

admin.site.register(Plataform)
admin.site.register(Director)
admin.site.register(Movie)