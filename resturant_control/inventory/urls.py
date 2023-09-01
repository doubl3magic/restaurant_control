from django.urls import path

from resturant_control.inventory.views import HomeView, IngredientsListView, MenuItemsListView, PurchasesListView, RestaurantFinanceView, \
    DeleteIngredientView, RecipeRequirementsListView, AddIngredientView, EditIngredientView, AddMenuItemView, \
    AddRecipeRequirementView, AddPurchaseView, EditMenuItemView, DeleteMenuItemView, \
    DeletePurchaseView, EditRecipeRequirementView, DeleteRecipeRequirementView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('ingredients/', IngredientsListView.as_view(), name='ingredients_list'),
    path('ingredients/add-ingredient/', AddIngredientView.as_view(), name='add_ingredient'),
    path('ingredients/edit-ingredient/<pk>/', EditIngredientView.as_view(), name='edit_ingredient'),
    path('ingredients/delete-ingredient/<pk>/', DeleteIngredientView.as_view(), name='delete_ingredient'),

    path('recipe-requirements/', RecipeRequirementsListView.as_view(), name='recipe_requirements'),
    path('recipe-requirements/add-requirement', AddRecipeRequirementView.as_view(), name='add_requirement'),
    path('recipe-requirements/edit-requirement/<pk>/', EditRecipeRequirementView.as_view(), name='edit_requirement'),
    path('recipe-requirements/delete-requirement/<pk>/',
         DeleteRecipeRequirementView.as_view(), name='delete_requirement'),

    path('menu-items/', MenuItemsListView.as_view(), name='menu_items'),
    path('menu-items/add-item/', AddMenuItemView.as_view(), name='add_item'),
    path('menu-items/edit-item/<pk>/', EditMenuItemView.as_view(), name='edit_item'),
    path('menu-items/delete-item/<pk>/', DeleteMenuItemView.as_view(), name='delete_item'),

    path('purchases/', PurchasesListView.as_view(), name='purchases'),
    path('purchases/add-purchase/', AddPurchaseView.as_view(), name='add_purchase'),
    path('purchases/delete-purchase/<pk>/', DeletePurchaseView.as_view(), name='delete_purchase'),

    path('restaurant-finance/', RestaurantFinanceView.as_view(), name='restaurant_finance'),
]
