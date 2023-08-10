from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import generic as views

from inventory.models import Ingredient, MenuItem, Purchase


class HomeView(views.TemplateView, LoginRequiredMixin):
    template_name = './inventory/index.html'


class IngredientsListView(views.ListView, LoginRequiredMixin):
    model = Ingredient
    template_name = './inventory/ingredients-list.html'


class MenuItemsListView(views.ListView, LoginRequiredMixin):
    model = MenuItem
    template_name = './inventory/menu-items.html'


class PurchasesListView(views.ListView, LoginRequiredMixin):
    model = Purchase
    template_name = './inventory/purchases.html'


class RestaurantFinanceView(views.TemplateView, LoginRequiredMixin):
    template_name = './inventory/restaurant-finance.html'

    def get_context_data(self, **kwargs):
        context = {
            'total_revenue':
                round(sum([p.calculate_revenue() for p in Purchase.objects.all()]), 2),
            'total_cost':
                round(sum([p.calculate_cost_item() for p in Purchase.objects.all()]), 2),
            'total_profit':
                round(sum([p.calculate_profit() for p in Purchase.objects.all()]), 2)
        }
        return context
