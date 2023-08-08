from django.contrib import admin

from inventory.models import Inventory, MenuItems, RecipeRequirements, Purchase


@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ('ingredient_name', 'available_qty', 'unit')


@admin.register(MenuItems)
class MenuItemsAdmin(admin.ModelAdmin):
    list_display = ('item', 'price')


@admin.register(RecipeRequirements)
class RecipeRequirementsAdmin(admin.ModelAdmin):
    list_display = ('menu_item', 'ingredient')


@admin.register(Purchase)
class RecipeRequirementsAdmin(admin.ModelAdmin):
    list_display = ('menu_item', 'purchase_time')
    list_filter = 'purchase_time'
