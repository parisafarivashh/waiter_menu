from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView

from .views import CallDeskWaiterView, WaiterTasksView

urlpatterns = [
    path('token', TokenObtainPairView.as_view(), name='token'),
    path('demand/<int:desk_id>', CallDeskWaiterView.as_view(), name='call_waiter'),
    path('demands/<int:id>', WaiterTasksView.as_view(), name='waiter_task'),
]

