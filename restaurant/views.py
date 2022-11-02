
# Create your views here.

from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import Ingredient,MenueItem,RecipeRequirement,Purchase
from django.urls import reverse_lazy
from .forms import MenueForm,InventoryForm,RecipeForm,PurchaseForm
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse

from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

def exit(request):
          return render(request,'inventory/exit.html')


def home(request):
          return render(request,'inventory/home.html')

class InventoryIngredients(ListView):
          model = Ingredient
          template_name = 'inventory/ingredient_left.html'


class MenueView(ListView):
          model = MenueItem
          template_name = 'inventory/menue_view.html'


class PurchaseView(ListView):
          model = Purchase
          template_name = 'inventory/purchase_view.html'


class RecipeView(ListView):
          model = RecipeRequirement
          template_name = 'inventory/recipe_view.html'

def profit(request):
          purchased_all = Purchase.objects.all()
          total_profit = 0 
          for item in purchased_all:
                    purchased = item.purchased_item
                    prices = MenueItem.objects.filter(title = purchased)
                    total = 0 
                    for num in prices:
                              total += num.price
                    total_profit += total  
          context = {'total_profit': total_profit}
          return render(request,'inventory/profit_view.html', context)


def cost(request):
          purchased_all = Purchase.objects.all()
          total_cost = 0
          for item in purchased_all:
                    purchased = item.purchased_item
                    costs = RecipeRequirement.objects.filter(menu_item = purchased)
                    total = 0 
                    for item in costs:
                              total += item.new_cost
                    total_cost += total 
          return render(request,'inventory/cost.html', {'total_cost':total_cost})


def revenue(request):
          purchased_all = Purchase.objects.all()
          total_profit = 0 
          total_cost = 0
          for item in purchased_all:
                    purchased = item.purchased_item
                    prices = MenueItem.objects.filter(title = purchased)
                    costs = RecipeRequirement.objects.filter(menu_item = purchased)
                    total_prices = 0 
                    total_costs = 0
                    for num in prices:
                              total_prices += num.price
                    total_profit += total_prices

                    for item in costs:
                              total_costs += item.new_cost
                    total_cost +=  total_costs
          context = {'revenue': total_profit - total_cost }
          return render(request,'inventory/revenue_view.html',context )



class DeleteIngredients(DeleteView):
          model = Ingredient
          template_name = 'inventory/delete_view.html'
          success_url = reverse_lazy('inventory')    
          
class UpdateIngredients(UpdateView):
          model = Ingredient
          form_class = InventoryForm
          template_name = 'inventory/ingredient_update.html'
          success_url = reverse_lazy('inventory') 

class UpdateMenue(UpdateView):
          model = MenueItem
          form_class = MenueForm
          template_name = 'inventory/menue_update.html'
          success_url = reverse_lazy('menue') 


class UpdateRecipe(UpdateView):
          model = RecipeRequirement
          form_class = RecipeForm
          template_name = 'inventory/recipe_update.html'
          success_url = reverse_lazy('recipe') 



class AddIngredients(CreateView):
          model = Ingredient
          form_class = InventoryForm
          template_name = 'inventory/ingredient_create.html'
          success_url = reverse_lazy('inventory') 

class AddMenue(CreateView):
          model = MenueItem
          form_class = MenueForm
          template_name = 'inventory/menue_create.html'
          success_url = reverse_lazy('menue') 


class AddRecipe(CreateView):
          model = RecipeRequirement
          form_class = RecipeForm
          template_name = 'inventory/recipe_create.html'
          success_url = reverse_lazy('recipe') 



class AddPurchase(CreateView):
          model = Purchase
          form_class = PurchaseForm
          template_name = 'inventory/purchase_create.html'
          success_url = reverse_lazy('purchase') 


class Signup(CreateView):
          form_class = UserCreationForm
          success_url = reverse_lazy('login')
          template_name = "registration/signup.html"

def logout_view(request):
          logout(request)
          return redirect('exit')
