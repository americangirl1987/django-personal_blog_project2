from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    desc = models.TextField()

    def __str__(self):
            return self.title
