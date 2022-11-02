
# Create your models here.
from email.policy import default
from django.db import models

# Create your models here.

from django.db import models

# Create your models here.

class Ingredient( models.Model):
    class Unit(models.IntegerChoices):
        Tbsp = 1, "Tbsp"
        Lbs = 2, "Lbs"
    unit = models.PositiveSmallIntegerField(choices=Unit.choices,default=Unit.Tbsp )
    name = models.CharField(max_length = 100)
    quantity = models.FloatField()
    unit_price = models.FloatField()

    def __str__(self):
          return self.name

class MenueItem(models.Model):
          title = models.CharField(max_length = 100)
          price = models.FloatField()

          def __str__(self):
                    return self.title

class RecipeRequirement(models.Model):
          menu_item = models.ForeignKey(MenueItem,on_delete=models.CASCADE)
          ingredient = models.ForeignKey(Ingredient,on_delete=models.CASCADE)
          quantity = models.FloatField()
          # cost = models.FloatField(default = 0 )
          @property
          def new_cost(self):
                    total_cost = 0 
                    for item in Ingredient.objects.filter(name = self.ingredient):
                              item_price = item.unit_price
                              item_total = self.quantity * item_price
                              total_cost += item_total
                    #return total_cost
                    # self.cost = self.total_cost
                    return total_cost

          def __str__(self):
                    return str(f'{self.menu_item} + {self.ingredient}')

class Purchase(models.Model):
          purchased_item = models.ForeignKey(MenueItem, on_delete=models.CASCADE)
          timestamp = models.DateField(auto_now = True)

          def __str__(self):
                    return str(self.purchased_item)

