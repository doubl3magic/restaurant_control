from django.db import models


class Inventory(models.Model):
    ingredient_name = models.CharField(max_length=200)
    available_qty = models.IntegerField()
    unit = models.CharField(max_length=4)
    price_unit = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f'{self.ingredient_name} ({self.unit} - Price: {self.price_unit} )'


class MenuItems(models.Model):
    item = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    recipe_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return f'{self.item} - {self.price}'


class RecipeRequirements(models.Model):
    menu_item = models.ForeignKey(MenuItems, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    qty = models.DecimalField(max_digits=6, decimal_places=1)


class Purchase(models.Model):
    menu_item = models.ForeignKey(MenuItems, on_delete=models.CASCADE)
    purchase_time = models.DateTimeField(auto_now=True)
