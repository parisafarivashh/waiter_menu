from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated

from ..models.desk import Desk
from ..models.demand import Demand
from ..serializers import CallWaiterSerializer, WaiterTasksSerializer


class CallDeskWaiterView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = CallWaiterSerializer
    queryset = Demand.objects.all()

    def perform_create(self, serializer):
        desk = get_object_or_404(Desk, id=self.kwargs['desk_id'])
        serializer.save(desk=desk)


class WaiterTasksView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = WaiterTasksSerializer
    queryset = Demand.objects.all()
    lookup_field = 'id'

    def perform_update(self, serializer):
        serializer.save(done_by=self.request.user)

