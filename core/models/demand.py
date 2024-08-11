from django.db import models


class Demand(models.Model):
    desk = models.ForeignKey('Desk', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, editable=False)

