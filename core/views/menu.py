from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from ..models import Item
from ..permissions import IsAdmin
from ..serializers import MenuCreateSerializers


class MenuCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated, IsAdmin]
    serializer_class = MenuCreateSerializers
    queryset = Item.objects.all()




