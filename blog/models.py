from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField


class Post(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=200)
    body = RichTextUploadingField()

    def __str__(self):
        return self.title
