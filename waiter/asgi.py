"""
ASGI config for waiter project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os

import django
from channels.routing import ProtocolTypeRouter, URLRouter

from django.core.asgi import get_asgi_application

from core.routing import websocket_urlpatterns

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'waiter.settings')
django.setup()


from waiter.middleware import JWTAuthMiddlewareStack


application = ProtocolTypeRouter({
    "http": get_asgi_application(),  # Django's standard HTTP application
    "websocket": JWTAuthMiddlewareStack(
        URLRouter(websocket_urlpatterns)
    ),
})

