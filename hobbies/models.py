from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Hobby(models.Model):
    users = models.ManyToManyField(User, related_name="hobbies")

    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to="hobby-image")

    def __unicode__(self):
        return self.name

class Resource(models.Model):
    hobby = models.ForeignKey(Hobby, related_name="resources")

    name = models.CharField(max_length=200)
    link = models.URLField()

    def __unicode__(self):
        return self.name
