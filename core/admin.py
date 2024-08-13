from django.contrib import admin

from .models import Desk, Demand, Category, Item, DeskWaiter


admin.site.register(Demand)
admin.site.register(Desk)
admin.site.register(Category)
admin.site.register(Item)
admin.site.register(DeskWaiter)

