from webbrowser import register

from django.contrib import admin

from .models import Desk, Demand, Category, Item, DeskWaiter


admin.site.register(Demand)
admin.site.register(Item)
admin.site.register(DeskWaiter)

class ItemAdminInline(admin.TabularInline):
    model = Item


@admin.register(Category)
class ItemAdmin(admin.ModelAdmin):
    inlines = [ItemAdminInline]


class DemandAdminInline(admin.StackedInline):
    model = Demand


@admin.register(Desk)
class DeskModelAdmin(admin.ModelAdmin):
    inlines = [DemandAdminInline]
