from datetime import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views


from resturant_control.inventory.forms import MenuItemForm, IngredientForm, RecipeReqForm, PurchaseForm
from resturant_control.inventory.models import Ingredient, MenuItem, Purchase, RecipeRequirements


class HomeView(views.TemplateView):
    template_name = './inventory/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['user'] = self.request.user.is_authenticated
        return context


# INGREDIENT VIEWS
class IngredientsListView(LoginRequiredMixin, views.ListView):
    model = Ingredient
    template_name = './inventory/ingredients/ingredients-list.html'


class AddIngredientView(LoginRequiredMixin, views.CreateView):
    form_class = IngredientForm
    template_name = 'inventory/ingredients/add-ingredient.html'
    success_url = reverse_lazy('ingredients_list')


class EditIngredientView(LoginRequiredMixin, views.UpdateView):
    model = Ingredient
    form_class = IngredientForm
    template_name = 'inventory/ingredients/edit-ingredient.html'
    success_url = reverse_lazy('ingredients_list')


class DeleteIngredientView(LoginRequiredMixin, views.DeleteView):
    model = Ingredient
    template_name = './inventory/ingredients/delete-ingredient.html'
    success_url = '/ingredients'


# MENU ITEMS VIEWS
class MenuItemsListView(LoginRequiredMixin, views.ListView):
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


class AddMenuItemView(LoginRequiredMixin, views.CreateView):
    model = MenuItem
    form_class = MenuItemForm
    template_name = 'inventory/menu_items/add-item.html'
    success_url = reverse_lazy('menu_items')


class EditMenuItemView(LoginRequiredMixin, views.UpdateView):
    model = MenuItem
    form_class = MenuItemForm
    template_name = 'inventory/menu_items/edit-menu-item.html'
    success_url = reverse_lazy('menu_items')


class DeleteMenuItemView(LoginRequiredMixin, views.DeleteView):
    model = MenuItem
    template_name = 'inventory/menu_items/delete-menu-item.html'
    success_url = reverse_lazy('menu_items')


# RECIPE REQUIREMENTS VIEWS
class RecipeRequirementsListView(LoginRequiredMixin, views.ListView):
    model = RecipeRequirements
    template_name = './inventory/recipe_requirements/recipe-requirements.html'


class AddRecipeRequirementView(LoginRequiredMixin, views.CreateView):
    model = RecipeRequirements
    form_class = RecipeReqForm
    template_name = 'inventory/recipe_requirements/add-recipe-req.html'
    success_url = reverse_lazy('recipe_requirements')


class EditRecipeRequirementView(LoginRequiredMixin, views.UpdateView):
    model = RecipeRequirements
    form_class = RecipeReqForm
    template_name = 'inventory/recipe_requirements/edit-recipe-req.html'
    success_url = reverse_lazy('recipe_requirements')


class DeleteRecipeRequirementView(LoginRequiredMixin, views.DeleteView):
    model = RecipeRequirements
    template_name = 'inventory/recipe_requirements/delete-recipe-req.html'
    success_url = reverse_lazy('recipe_requirements')


class PurchasesListView(LoginRequiredMixin, views.ListView):
    model = Purchase
    template_name = './inventory/purchases/purchases.html'


class AddPurchaseView(LoginRequiredMixin, views.CreateView):
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


class DeletePurchaseView(LoginRequiredMixin, views.DeleteView):
    model = Purchase
    template_name = 'inventory/purchases/delete-purchase.html'
    success_url = reverse_lazy('purchases')


class RestaurantFinanceView(LoginRequiredMixin, views.TemplateView):
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
