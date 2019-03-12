from django.db import models


# Create your models here.

class PostModel(models.Model):
    postSubject = models.CharField(max_length=250)
    postText = models.TextField(max_length=2000, default="")
    imageURL = models.CharField(max_length=800, default="")


class RelatedItemsModel(models.Model):
    postSubject = models.CharField(max_length=250)
    postText = models.TextField(max_length=2000, default="")
    imageURL = models.CharField(max_length=800, default="")
