from django.db import models


class Ingredient(models.Model):
    ingredient_name = models.CharField(max_length=200)
    available_qty = models.IntegerField()
    unit = models.CharField(max_length=4)
    price_unit = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f'{self.ingredient_name} ({self.unit} - Price: {self.price_unit} )'


class MenuItem(models.Model):
    item = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    recipe_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return f'{self.item} - {self.price}'


class RecipeRequirements(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    qty = models.DecimalField(max_digits=6, decimal_places=1)


class Purchase(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    purchase_time = models.DateTimeField(auto_now=True)

    """
        Calculates the revenue of the menu_item
    """
    def calculate_revenue(self):
        return self.menu_item.price

    """
        Calculates the price of the ingredients used for an menu item
    """
    def calculate_cost_item(self):
        recipe_objects = RecipeRequirements.objects.filter(menu_item=self.menu_item)
        return float(sum([item.ingredient * item.qty for item in recipe_objects]))

    """
        Calculates the profit made from a product
    """
    def calculate_profit(self):
        return float(self.calculate_revenue() - self.calculate_cost_item())