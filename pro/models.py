from django.db import models

# Create your models her

class Project(models.Model):
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=200)
    image = models.ImageField(upload_to='pro/images/')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title
