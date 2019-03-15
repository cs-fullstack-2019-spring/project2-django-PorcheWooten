from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class PostModel(models.Model):
    postSubject = models.CharField(max_length=250)
    postText = models.TextField(max_length=2000, default="")
    wiki_post_image = models.ImageField(blank=True, null=True, upload_to="images/%Y/%m/%d/")
    foreignKeyToPost = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)

    def __str__(self):
        return self.postSubject

class RelatedItemsModel(models.Model):
    postSubject = models.CharField(max_length=250)
    postText = models.TextField(max_length=2000, default="")
    wiki_post_image = models.ImageField(blank=True, null=True, upload_to="images/%Y/%m/%d/")
    relatedItemForeignKey = models.ForeignKey(PostModel, on_delete=models.CASCADE,null=True, blank=True)

    def __str__(self):
        return self.postSubject



















class WikiUserModel(models.Model):
    username = models.CharField(max_length=20)
    password1 = models.CharField(max_length=10)
    password2 = models.CharField(max_length=10)
    foreignKeyToUser = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.username