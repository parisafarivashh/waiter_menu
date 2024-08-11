from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


channel = get_channel_layer()


class Demand(models.Model):
    desk = models.ForeignKey('Desk', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, editable=False)


@receiver(signal=post_save, sender=Demand)
def send_notif(created, sender, instance, **kwargs):
    if created:
        async_to_sync(channel.group_send)(
            instance.desk.code,
            {'type': 'request_waiter', 'code': instance.desk.code}
        )

