from asgiref.sync import sync_to_async
from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncJsonWebsocketConsumer

from core.apps import logger


class WaitingConsumer(AsyncJsonWebsocketConsumer):

    async def connect(self):
        user = self.scope.get('user')
        if user is None:
            logger.error(msg='User is not Authenticated')
            await self.close(code=4001)

        desks_waiters = await self.get_desks(user)
        for desk_waiter in desks_waiters:
            await self.channel_layer.group_add(
                desk_waiter['desk__code'],  # name group
                self.channel_name,
            )
            print(self.channel_name)
        await self.accept()

    async def request_waiter(self, event):
        await self.send_json(f'{event["code"]} you have request')

    async def request_done(self, event):
        await self.send_json(f"{event['code']} done by {event['done_by']}")

    @database_sync_to_async
    def get_desks(self, user):
        from .models.desk import DeskWaiter
        return list(DeskWaiter.objects.filter(waiter=user).values('desk__code').all())

