from urllib.parse import parse_qs

from asgiref.sync import sync_to_async
from channels.auth import AuthMiddlewareStack
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser
from django.db import close_old_connections
from jwt import InvalidSignatureError, ExpiredSignatureError, DecodeError
import jwt

from waiter import settings

User = get_user_model()


class JWTAuthMiddleware:

    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
        close_old_connections()
        try:
            query_string = scope.get('query_string').decode('utf-8')
            print(query_string[6:])
            token = parse_qs(query_string).get('token', [None])[0]
            print(token)

            data = jwt.decode(jwt=token, key=settings.SECRET_KEY, algorithms=["HS256"])
            scope['user'] = await sync_to_async(self.get_user)(data['user_id'])
        except (TypeError, KeyError, InvalidSignatureError,
                ExpiredSignatureError, DecodeError) as e:
            print(e)
            scope['user'] = AnonymousUser()
        return await self.app(scope, receive, send)

    def get_user(self, user_id):
        """Return the user based on user id."""
        try:
            return User.objects.get(id=user_id)
        except User.DoesNotExist:
            return AnonymousUser()


def JWTAuthMiddlewareStack(app):
    """This function wrap channels authentication stack with JWTAuthMiddleware."""
    return JWTAuthMiddleware(AuthMiddlewareStack(app))

