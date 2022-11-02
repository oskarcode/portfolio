from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.exit, name = 'restaurant'),
    path("home/", views.home, name = 'home' ),
    path("inventory/", views.InventoryIngredients.as_view(), name = 'inventory' ),
    path("menue/", views.MenueView.as_view(), name = 'menue' ), 
    path("purchase/", views.PurchaseView.as_view(), name = 'purchase'),
    path("profit/", views.profit, name = 'profit'),
    path("recipe/", views.RecipeView.as_view(), name = 'recipe'),
    path("cost/", views.cost, name = 'cost'),
    path("revenue/", views.revenue, name = 'revenue'),
    path("inventory/<pk>/delete/", views.DeleteIngredients.as_view(), name = 'delete-ingredient'),
    path("inventory/<pk>/update/", views.UpdateIngredients.as_view(), name = 'update-ingredient'),
    path("menue/<pk>/update/", views.UpdateMenue.as_view(), name = 'update-menue'),
    path("recipe/<pk>/update/", views.UpdateRecipe.as_view(), name = 'update-recipe'),
    path("inventory/add/", views.AddIngredients.as_view(), name = 'add-ingredient'),
    path("menue/add/", views.AddMenue.as_view(), name = 'add-menue'),
    path("recipe/add/", views.AddRecipe.as_view(), name = 'add-recipe'),
    path("purchase/add/", views.AddPurchase.as_view(), name = 'add-purchase'),
    path("account/",include("django.contrib.auth.urls")),
    path("signup/",views.Signup.as_view(), name = 'signup'),
    path("logout/",views.logout_view, name = 'logout'),
]
