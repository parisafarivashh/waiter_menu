from django.db import models


class Item(models.Model):
    category = models.ForeignKey('Category', on_delete=models.PROTECT)
    title = models.CharField(max_length=64, null=False, blank=False)
    description = models.CharField(max_length=255, blank=True, null=True)
    price = models.IntegerField(null=True, blank=True)
    thumbnail = models.ImageField(null=True, blank=True)

