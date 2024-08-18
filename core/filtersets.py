from django_filters.rest_framework import FilterSet, filters

from core.models import Item


class ItemFilterset(FilterSet):
    ingredients = filters.CharFilter(method='filter_by_ingredient')

    def filter_by_ingredient(self, queryset, name, value):
        return queryset.filter(ingredients__icontains=value)

    class Meta:
        model = Item
        fields = '__all__'