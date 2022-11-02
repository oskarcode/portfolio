from django.shortcuts import render
# Create your views here.
from django.shortcuts import render,redirect
from .models import Owner, Patient
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.http import Http404,HttpResponse
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from .forms import OwnerUpdateForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin




def home(request):
   context = {"name": request.user }
   return render(request, "vetoffice/home.html", context)

class OwnerList(ListView):
  model = Owner
  template_name = "vetoffice/owner_list.html"

class PatientList(ListView):
  model = Patient
  template_name = "vetoffice/patient_list.html"

class OwnerCreate(CreateView):
  model = Owner
  template_name = "vetoffice/owner_create_form.html"
  fields = ["first_name", "last_name", "phone"]
  success_url = reverse_lazy('vetoffice')
  success_message = 'Successfully added'

class PatientCreate(CreateView):
  model = Patient
  template_name = "vetoffice/patient_create_form.html"
  fields = ["animal_type", "breed", "pet_name", "age", "owner"]
  success_url = reverse_lazy('vetoffice')
  success_message = 'Successfully added'

# class OwnerUpdate(UpdateView):
#   model = Owner
#   template_name = "vetoffice/owner_update_form.html"
#   fields = ["first_name", "last_name", "phone"]
#   success_url = "/vetoffice/owner/list"

class OwnerUpdate(UpdateView):
  model = Owner
  template_name = "vetoffice/owner_update_form.html"
  form_class = OwnerUpdateForm
  success_url = reverse_lazy('vetoffice')
  success_message = 'Successfully added'



class PatientUpdate(UpdateView):
  model = Patient
  template_name = "vetoffice/patient_update_form.html"
  fields = ["animal_type", "breed", "pet_name", "age", "owner"]
  success_url = reverse_lazy('vetoffice')
  success_message = 'Successfully added'

class OwnerDelete(DeleteView):
  model = Owner
  template_name = "vetoffice/owner_delete_form.html"
  success_url = reverse_lazy('vetoffice')
  success_message = 'Successfully added'

class PatientDelete(DeleteView):
  model = Patient
  template_name = "vetoffice/patient_delete_form.html"
  success_url = reverse_lazy('vetoffice')
  success_message = 'Successfully added'


# def login_view(request):
#   context = {
#     "login_view": "active"
#   }
#   if request.method == "POST":
#     username = request.POST["username"]
#     password = request.POST["password"]
#     user = authenticate(request, username=username, password=password)
#     if user is not None:
#       # Add your code below:
#       login(request,user)
      
#       return redirect("home")
#     else:
#       return HttpResponse("invalid credentials")
#   return render(request, "registration/login.html", context)


def logout_view(request):
  logout(request)
  return redirect('vetoffice')