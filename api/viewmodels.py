from django.db import models


def image_path(instance, filename):
    return 'balcony_{1}'.format(filename)


class BalconyViewModel(models.Model):
    img = models.ImageField(upload_to=image_path, blank=True, null=False)
    uri = models.CharField(max_length=255)
    height = models.PositiveIntegerField()
    width = models.PositiveIntegerField()
