from django.db import models


class Movie(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    year = models.IntegerField()
    image = models.ImageField(upload_to='images/',blank=True,null=True)

    def __str__(self):
        return self.name