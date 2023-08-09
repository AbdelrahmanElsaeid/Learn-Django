from django.db import models

# Create your models here.


class PostModel(models.Model):
    title = models.CharField(max_length=120)
    active = models.BooleanField(default=True)
    content = models.TextField(max_length=300)