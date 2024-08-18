from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


channel = get_channel_layer()


class Item(models.Model):
    category = models.ForeignKey('Category', on_delete=models.PROTECT)
    title = models.CharField(max_length=64, null=False, blank=False)
    description = models.CharField(max_length=255, blank=True, null=True)
    price = models.IntegerField(null=True, blank=True)
    ingredients = ArrayField(
        models.CharField(max_length=12, blank=True),
        default=list,
    )


@receiver(post_save, sender=Item)
def waiter_notif(created, sender, instance, *args, **kwargs):
    from ..serializers import MenuCreateSerializers

    if created:
        async_to_sync(channel.group_send)(
            'restaurant_menu',
            {
                'type': 'add_item',
                'item': MenuCreateSerializers(instance).data
            }
        )

