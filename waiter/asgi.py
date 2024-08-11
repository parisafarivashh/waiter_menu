"""
ASGI config for waiter project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path

from django.core.asgi import get_asgi_application

from core.consumers import WaitingConsumer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'waiter.settings')
print('1'*99)

application = ProtocolTypeRouter({
    "http": get_asgi_application(),  # Django's standard HTTP application
    "websocket": AuthMiddlewareStack(
        URLRouter([
            path('waiting', WaitingConsumer.as_asgi()),
        ])
    ),
})

