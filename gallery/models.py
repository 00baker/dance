from django.db import models
from django.db.models import permalink

# Create your models here.

class Images(models.Model):
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

