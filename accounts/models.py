from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
# Create your models here.
class User(AbstractUser):
    email = models.EmailField(_("email address"), blank=True, unique=True)
    bio=models.TextField(blank=True,null=True,help_text='Give some information about yourself')
    
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

class InstagramUser(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class InstagramFollow(models.Model):
    user_id = models.ForeignKey(InstagramUser, on_delete=models.CASCADE)
    followers = models.CharField(max_length=100)
    following = models.CharField(max_length=100)