from django.conf import settings
from django.db import models


class Desk(models.Model):
    code = models.CharField(max_length=16, null=False, blank=False)
    title = models.CharField(max_length=64, null=False, blank=False)
    waiter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.code} - {self.title}"

