from django.db import models
from django.db.models import permalink

# Create your models here.

class Image(models.Model):
    image = models.FileField(upload_to='images')
    posted_on = models.DateTimeField(auto_now_add=True)
    caption = models.CharField(max_length=500)
    category = models.ForeignKey('gallery.Category')
    slug = models.SlugField(max_length=200)

    def __str__(self):
        return self.caption


class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)

    def __str__(self):
        return self.title

    @permalink
    def get_absolute_url(self):
        return ('view_category', None, { 'slug': self.slug })

    class Meta:
        verbose_name_plural = "categories"

class Video(models.Model):
    title = models.CharField(max_length=200)
    video = models.CharField(max_length=500)
    category = models.ForeignKey('gallery.Category')
    posted_on = models.DateTimeField(auto_now_add=True)
    video_id = models.CharField(max_length=200)


    def __str__(self):
        return self.title


