from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class PostModel(models.Model):
    postSubject = models.CharField(max_length=250)
    postText = models.TextField(max_length=2000, default="")
    imageURL = models.CharField(max_length=800, default="")
    postForeignKey = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True, unique=True)
    def __str__(self):
        return self.postSubject

class RelatedItemsModel(models.Model):
    postSubject = models.CharField(max_length=250)
    postText = models.TextField(max_length=2000, default="")
    imageURL = models.CharField(max_length=800, default="")
