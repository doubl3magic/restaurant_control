from django.db import models


class Ingredient(models.Model):
    INGREDIENT_NAME_MAX_LENGTH = 200
    UNIT_MAX_LENGTH = 4
    PRICE_UNIT_MAX_DIGITS = 6
    PRICE_UNIT_DECIMAL_PLACES = 2

    ingredient_name = models.CharField(max_length=INGREDIENT_NAME_MAX_LENGTH)
    available_qty = models.IntegerField()
    unit = models.CharField(max_length=UNIT_MAX_LENGTH)
    price_unit = models.DecimalField(max_digits=PRICE_UNIT_MAX_DIGITS, decimal_places=PRICE_UNIT_DECIMAL_PLACES)

    def __str__(self):
        return f'{self.ingredient_name} ({self.unit} - Price: {self.price_unit} )'


class MenuItem(models.Model):
    ITEM_MAX_LENGTH = 200
    DESCRIPTION_MAX_LENGTH = 500
    CATEGORY_MAX_LENGTH = 2
    PRICE_MAX_DIGITS = 6
    PRICE_DECIMAL_PLACES = 2

    STARTER = 'SR'
    MAIN_COURSE = 'MC'
    SOUP = 'SP'
    DESSERT = 'DT'
    ALCOHOL = 'AL'
    BEVERAGE = 'BE'
    WATER = 'W'

    MENU_ITEM_CATEGORY_CHOICES = {
        (STARTER, 'Starter'),
        (MAIN_COURSE, 'Main Course'),
        (SOUP, 'Soup'),
        (DESSERT, 'Desert'),
        (ALCOHOL, 'Alcohol'),
        (BEVERAGE, 'Beverage'),
        (WATER, 'W')
    }

    item = models.CharField(max_length=ITEM_MAX_LENGTH)
    price = models.DecimalField(max_digits=PRICE_MAX_DIGITS, decimal_places=PRICE_DECIMAL_PLACES)
    description = models.TextField(max_length=DESCRIPTION_MAX_LENGTH, blank=True, null=True)
    recipe_url = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=CATEGORY_MAX_LENGTH, choices=MENU_ITEM_CATEGORY_CHOICES)

    def __str__(self):
        return f'{self.item} - {self.price}'


class RecipeRequirements(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    qty = models.DecimalField(max_digits=6, decimal_places=1)

    class Meta:
        ordering = ["menu_item"]


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
        return float(sum([item.ingredient.price_unit * item.qty for item in recipe_objects]))

    """
        Calculates the profit made from a product
    """

    def calculate_profit(self):
        return float(self.calculate_revenue()) - self.calculate_cost_item()
