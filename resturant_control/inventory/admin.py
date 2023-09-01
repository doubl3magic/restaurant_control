from django.contrib import admin

from resturant_control.inventory.models import Ingredient, MenuItem, RecipeRequirements, Purchase


@admin.register(Ingredient)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ('ingredient_name', 'available_qty', 'unit')


@admin.register(MenuItem)
class MenuItemsAdmin(admin.ModelAdmin):
    list_display = ('item', 'price')


@admin.register(RecipeRequirements)
class RecipeRequirementsAdmin(admin.ModelAdmin):
    list_display = ('menu_item', 'ingredient')


@admin.register(Purchase)
class RecipeRequirementsAdmin(admin.ModelAdmin):
    list_display = ('menu_item', 'purchase_time')
    list_filter = ('purchase_time',)

