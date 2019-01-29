from django.db import models
from django.contrib.auth.models import User


SCREENSHOT_TYPE = ((1, 'Simple'), (2, 'FullScreen'))
SOURCE_TYPE = ((1, 'List'), (2, 'File'))


class Requesting(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    r_type = models.IntegerField(default = 1, choices = SCREENSHOT_TYPE)
    source = models.IntegerField(default = 1, choices = SOURCE_TYPE)


class Screenshots(models.Model):
    requesting = models.ForeignKey(Requesting, null = True, on_delete=models.PROTECT)
    url = models.URLField(null=True)
    image = models.ImageField(upload_to='images', null=True)
    title = models.CharField(max_length = 150, null = True)