from django.urls import path

from core.consumers import WaitingConsumer


websocket_urlpatterns = [
    path('waiting', WaitingConsumer.as_asgi()),
]

