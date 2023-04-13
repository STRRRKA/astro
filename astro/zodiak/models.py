from django.db import models

# Create your models here.
class star(models.Model):
    rusName = models.CharField(max_length=20)
    latName = models.CharField(max_length=20)
    sokr = models.CharField(max_length=20)
    square = models.CharField(max_length=20)