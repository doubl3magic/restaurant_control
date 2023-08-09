from django.shortcuts import render
from django.views import generic as views

from inventory.models import Ingredient, MenuItem, Purchase


class IngredientsListView(views.ListView):
    model = Ingredient
    template_name = ''


class MenuItemsListView(views.ListView):
    model = MenuItem
    template_name = ''


class PurchasesListView(views.ListView):
    model = Purchase
    template_name = ''


class RestaurantFinanceView(views.TemplateView):
    template_name = ''

    def get_context_data(self, **kwargs):
        pass