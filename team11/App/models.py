from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import *


# Create your models here.


class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)

    # teacher model that inherit his auth id from user Table
    def __str__(self):
        return self.user.username



class AdminMessage(models.Model):
    messageTitle = models.TextField(default="")
    messageContent = models.TextField(default="")

    def __str__(self):
        return self.messageTitle







