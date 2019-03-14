from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class PostModel(models.Model):
    postSubject = models.CharField(max_length=250)
    postText = models.TextField(max_length=2000, default="")
    imageURL = models.CharField(max_length=800, default="")
    postForeignKey = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)

    def __str__(self):
        return self.postSubject

class RelatedItemsModel(models.Model):
    postSubject = models.CharField(max_length=250)
    postText = models.TextField(max_length=2000, default="")
    imageURL = models.CharField(max_length=800, default="")
    relatedItemForeignKey = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)

    def __str__(self):
        return self.postSubject

class WikiUserModel(models.Model):
    username = models.CharField(max_length=20)
    password1 = models.CharField(max_length=10)
    password2 = models.CharField(max_length=10)
    userForeignKey = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.username