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

    def get_context_data(self, **kwargs):
        context = {
            'starters': MenuItem.objects.filter(category='SR'),
            'main_course': MenuItem.objects.filter(category='MC'),
            'soups': MenuItem.objects.filter(category='SP'),
            'desserts': MenuItem.objects.filter(category='DT'),
            'alcohol': MenuItem.objects.filter(category='AL'),
            'beverage': MenuItem.objects.filter(category='BE'),
            'water': MenuItem.objects.filter(category='W'),
        }
        return context


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
