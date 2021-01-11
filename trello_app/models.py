from django.db import models
from django.contrib.auth.models import User

class List(models.Model):
  title = models.CharField(max_length=300)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.title
  

# Create your models here.
