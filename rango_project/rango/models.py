from django.db import models

# Create your models here.
from django.utils.text import slugify


class Category (models.Model):
    name = models.CharField(max_length=50, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

class Page (models.Model):
    title = models.CharField(max_length=50)
    category = models.ForeignKey(Category)
    url = models.URLField(default="")
    views = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title

