from django.db import models
from django.contrib.auth.models import User

class List(models.Model):
  title = models.CharField(max_length=100)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.title

class Card(models.Model):
  title = models.CharField(max_length=200)
  description = models.TextField()
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  list = models.ForeignKey(List, on_delete=models.CASCADE)
  
  def __str__(self):
    return self.title


# Create your models here.
