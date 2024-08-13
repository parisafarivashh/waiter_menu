from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=64, null=False, blank=False)
    parent = models.ForeignKey('self', on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.title}"

