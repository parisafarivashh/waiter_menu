from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from ..models import Category
from ..permissions import IsAdmin
from ..serializers import CategorySerializer


class CategoryView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, IsAdmin]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

