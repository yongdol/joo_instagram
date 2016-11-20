from django.db import models
from django.conf import settings


class Photo(models.Model):
    image = models.ImageField(upload_to='photo', blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    content = models.TextField(blank=True)
    tags = models.ManyToManyField('PhotoTag')
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, through='PhotoLike', related_name='photo_set_like_users')

class PhotoTag(models.Model):
    title = models.CharField(max_length=200)


class PhotoComment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    content = models.TextField()


class PhotoLike(models.Model):
    photo = models.ForeignKey(Photo)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    created_date = models.DateTimeField(auto_now_add=True)

