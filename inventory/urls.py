from django.urls import path

from inventory.views import HomeView, IngredientsListView, MenuItemsListView, PurchasesListView, RestaurantFinanceView, \
    DeleteIngredientView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('ingredients/', IngredientsListView.as_view(), name='ingredients_list'),
    path('menu-items/', MenuItemsListView.as_view(), name='menu_items'),
    path('purchases/', PurchasesListView.as_view(), name='purchases'),
    path('restaurant-finance/', RestaurantFinanceView.as_view(), name='restaurant_finance'),
    path('ingredients/delete-ingredient/<pk>', DeleteIngredientView.as_view(), name='delete_ingredient')
]
