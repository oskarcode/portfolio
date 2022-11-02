
from dataclasses import fields
from django import forms
from .models import Ingredient,MenueItem,RecipeRequirement,Purchase



class MenueForm(forms.ModelForm):
     class Meta:
          model = MenueItem
          fields = "__all__"


class InventoryForm(forms.ModelForm):
     class Meta:
          model = Ingredient
          fields = "__all__"

class RecipeForm (forms.ModelForm):
     class Meta:
          model = RecipeRequirement
          fields = "__all__"


class PurchaseForm (forms.ModelForm):
     class Meta:
          model = Purchase
          fields = "__all__"
