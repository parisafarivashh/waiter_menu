from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from ..filtersets import ItemFilterset
from ..models import Item
from ..permissions import IsAdmin
from ..serializers import MenuCreateSerializers


class MenuCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, IsAdmin]
    serializer_class = MenuCreateSerializers
    filter_backends = [DjangoFilterBackend]
    filterset_class = ItemFilterset
    queryset = Item.objects.all()




