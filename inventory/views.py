from datetime import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

from inventory.forms import MenuItemForm, IngredientForm, RecipeReqForm, PurchaseForm
from inventory.models import Ingredient, MenuItem, Purchase, RecipeRequirements


class HomeView(views.TemplateView, LoginRequiredMixin):
    template_name = './inventory/index.html'


# INGREDIENT VIEWS
class IngredientsListView(views.ListView, LoginRequiredMixin):
    model = Ingredient
    template_name = './inventory/ingredients/ingredients-list.html'


class AddIngredientView(views.CreateView, LoginRequiredMixin):
    form_class = IngredientForm
    template_name = 'inventory/ingredients/add-ingredient.html'
    success_url = reverse_lazy('ingredients_list')


class EditIngredientView(views.UpdateView, LoginRequiredMixin):
    model = Ingredient
    form_class = IngredientForm
    template_name = 'inventory/ingredients/edit-ingredient.html'
    success_url = reverse_lazy('ingredients_list')


class DeleteIngredientView(views.DeleteView, LoginRequiredMixin):
    model = Ingredient
    template_name = './inventory/ingredients/delete-ingredient.html'
    success_url = '/ingredients'


# MENU ITEMS VIEWS
class MenuItemsListView(views.ListView, LoginRequiredMixin):
    model = MenuItem
    template_name = './inventory/menu_items/menu-items.html'

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


class AddMenuItemView(views.CreateView, LoginRequiredMixin):
    model = MenuItem
    form_class = MenuItemForm
    template_name = 'inventory/menu_items/add-item.html'
    success_url = reverse_lazy('menu_items')


class EditMenuItemView(views.UpdateView, LoginRequiredMixin):
    model = MenuItem
    form_class = MenuItemForm
    template_name = 'inventory/menu_items/edit-menu-item.html'
    success_url = reverse_lazy('menu_items')


class DeleteMenuItemView(views.DeleteView, LoginRequiredMixin):
    model = MenuItem
    template_name = 'inventory/menu_items/delete-menu-item.html'
    success_url = reverse_lazy('menu_items')


# RECIPE REQUIREMENTS VIEWS
class RecipeRequirementsListView(views.ListView, LoginRequiredMixin):
    model = RecipeRequirements
    template_name = './inventory/recipe_requirements/recipe-requirements.html'


class AddRecipeRequirementView(views.CreateView, LoginRequiredMixin):
    model = RecipeRequirements
    form_class = RecipeReqForm
    template_name = 'inventory/recipe_requirements/add-recipe-req.html'
    success_url = reverse_lazy('recipe_requirements')


class EditRecipeRequirementView(views.UpdateView, LoginRequiredMixin):
    model = RecipeRequirements
    form_class = RecipeReqForm
    template_name = 'inventory/recipe_requirements/edit-recipe-req.html'
    success_url = reverse_lazy('recipe_requirements')


class DeleteRecipeRequirementView(views.DeleteView, LoginRequiredMixin):
    model = RecipeRequirements
    template_name = 'inventory/recipe_requirements/delete-recipe-req.html'
    success_url = reverse_lazy('recipe_requirements')


class PurchasesListView(views.ListView, LoginRequiredMixin):
    model = Purchase
    template_name = './inventory/purchases/purchases.html'


class AddPurchaseView(views.CreateView, LoginRequiredMixin):
    model = Purchase
    form_class = PurchaseForm
    template_name = './inventory/purchases/add-purchase.html'
    success_url = reverse_lazy('purchases')

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            menu_item = form.cleaned_data['menu_item']
            timestamp = datetime.now()
            new_purchase = Purchase()
            new_purchase.menu_item = menu_item
            new_purchase.purchase_time = timestamp
            new_purchase.save()
            requirements_purchase = RecipeRequirements.objects.filter(menu_item=menu_item)
            for requirement in requirements_purchase:
                required_qty = requirement.qty
                ingredient = Ingredient.objects.get(ingredient_name=requirement.ingredient.ingredient_name)
                ingredient.available_qty -= required_qty
                ingredient.save()
            return HttpResponseRedirect('/purchases')
        return render(request, self.template_name, {'form': form})


class DeletePurchaseView(views.DeleteView, LoginRequiredMixin):
    model = Purchase
    template_name = 'inventory/purchases/delete-purchase.html'
    success_url = reverse_lazy('purchases')


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
