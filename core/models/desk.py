from django.contrib.auth.models import User
from django.db import models


class Desk(models.Model):
    code = models.CharField(max_length=16, null=False, blank=False)
    title = models.CharField(max_length=64, null=False, blank=False)

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.code} - {self.title}"


class DeskWaiter(models.Model):
    waiter = models.ForeignKey(User, on_delete=models.PROTECT)
    desk = models.ForeignKey(Desk, on_delete=models.PROTECT)

    class Meta:
        db_table = 'desk_waiter'
        indexes = [
            models.Index(fields=['waiter'], name='waiter_index')
        ]

