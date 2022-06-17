from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    slug = models.SlugField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_published = models.DateTimeField(auto_now_add=True)
    #author = models.
    #thumbnail = models.

    def __str__(self):
        return self.title