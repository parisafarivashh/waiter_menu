from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from rest_framework import serializers

from .models.demand import Demand


channel = get_channel_layer()


class CallWaiterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Demand
        fields = ['id', 'desk']
        extra_kwargs = {'desk': {'read_only': True}}


class WaiterTasksSerializer(serializers.ModelSerializer):

    class Meta:
        model = Demand
        fields = ['id', 'done', 'done_by']
        extra_kwargs = {
            'done_by': {'read_only': True},
        }

    def update(self, instance, validated_data):
        response = super().update(instance, validated_data)
        async_to_sync(channel.group_send)(
            instance.desk.code,
            {
                'type': 'request_done',
                'code': instance.desk.code,
                'done_by': self.context['request'].user
            }
        )
        return response


