from django import forms
from django.core.exceptions import ValidationError

from inventory.models import Ingredient, RecipeRequirements, MenuItem, Purchase


class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = '__all__'


class RecipeReqForm(forms.ModelForm):
    class Meta:
        model = RecipeRequirements
        fields = '__all__'


class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = '__all__'


class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = '__all__'

    def clean_menu_item(self):
        menu_item = self.cleaned_data['menu_item']
        item_requirements = RecipeRequirements.objects.filter(menu_item=menu_item)
        if not item_requirements:
            raise ValidationError(f"There is no recipe for {menu_item}")
        for requirement in item_requirements:
            required_qty = requirement.qty
            ingredient = Ingredient.objects.get(ingredient_name=requirement.ingredient.ingredient_name)
            if not ingredient:
                raise ValidationError(f"The ingredient {ingredient} is not available!")
            current_qty = ingredient.available_qty
            if current_qty < required_qty:
                raise ValidationError(f"Not enough {ingredient} left!")
            return menu_item
