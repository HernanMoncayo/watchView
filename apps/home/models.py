# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Plataform (models.Model):
  name = models.CharField(max_length=50)
  icon = models.ImageField(upload_to='icons/')
  price = models.IntegerField()
  
  def __str__(self):
    return self.name

class Director (models.Model): 
  name = models.CharField(max_length=50)
  age = models.IntegerField()
  nationality = models.CharField(max_length=60)

  def __str__(self): 
    return self.name

class Movie (models.Model):
  title = models.CharField(max_length=50)
  description = models.TextField()
  gender = models.CharField(max_length=50)
  duration = models.IntegerField()
  cover = models.ImageField(upload_to='covers/')
  year = models.DateField()
  ranking = models.IntegerField()
  director = models.ForeignKey('Director', on_delete=models.PROTECT,related_name='get_directors' )
  plataform = models.ForeignKey('Plataform', on_delete=models.PROTECT,related_name='get_plataformas' )
  
  def __str__(self):
    return self.title

