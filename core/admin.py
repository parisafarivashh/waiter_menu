from django.contrib import admin

# Register your models here.
from .models import Desk, Demand, Category, Item

admin.site.register(Demand)
admin.site.register(Desk)
admin.site.register(Category)
admin.site.register(Item)

