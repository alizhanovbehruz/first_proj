from django.db import models


# Create your models here.

class Creator(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    tg_id = models.CharField(max_length=20)
    til = models.CharField(max_length=10, blank=True, null=True, default='uz')

    def __str__(self):
        return self.name


class author(models.Model):
    name = models.CharField(max_length=100)
    zanjir = models.CharField(max_length=200)
    price = models.FloatField(default=0)
    til = models.CharField(max_length=10, blank=True, null=True, default='uz')
    tg_id = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class channel(models.Model):
    name = models.CharField(max_length=200)
    channel_url = models.URLField()
    channel_id = models.CharField(max_length=30)
