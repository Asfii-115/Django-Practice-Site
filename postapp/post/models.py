from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  text = models.TextField(max_length=125)
  photo = models.ImageField(upload_to='photos/', blank=True, null=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return f"{self.user.username} - {self.text[:10]}"

class Profile(models.Model):
  name = models.CharField(max_length=125)
  surname = models.CharField(max_length=125)
  bio =  models.TextField(max_length=250)
  phone =  models.CharField(max_length=125)
  user = models.OneToOneField(User, on_delete=models.CASCADE)    

  def __str__(self):
    return self.user.username





