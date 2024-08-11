from asgiref.sync import sync_to_async
from channels.generic.websocket import AsyncJsonWebsocketConsumer

from core.apps import logger


class WaitingConsumer(AsyncJsonWebsocketConsumer):

    async def connect(self):
        user = self.scope.get('user')
        if user is None:
            logger.error(msg='User is not Authenticated')
            await self.close(code=4001)

        desks = await sync_to_async(self.get_desks)(user)
        for desk in desks:
            await self.channel_layer.group_add(
                desk.code,  # name group
                self.channel_name,
            )
        await self.accept()

    async def request_waiter(self, event):
        await self.send_json(event['code'])

    @staticmethod
    def get_desks(user):
        from .models.desk import Desk
        return Desk.objects.filter(waiter=user).all()
