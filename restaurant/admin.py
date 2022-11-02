from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Ingredient,MenueItem,RecipeRequirement,Purchase

# Register your models here.

admin.site.register(Ingredient)
admin.site.register(MenueItem)
admin.site.register(RecipeRequirement)
admin.site.register(Purchase)