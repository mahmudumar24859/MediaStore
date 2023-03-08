from django.db import models

# Create your models here.


class SahihMuslim(models.Model):
    title = models.CharField(max_length=200, unique=True)
    artist = models.CharField(max_length=150)
    audio_file = models.FileField()

    def __str__(self):
        return self.title
