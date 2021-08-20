from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView
from .models import Profile
from django.shortcuts import redirect, render
from .forms import AddUserForm, Register, UserAddForm
from django.http import HttpResponseRedirect, request
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.utils.decorators import method_decorator

def index(request):
   return render(request, 'pages/home.html')
def register(request):
   form = Register()
   if request.method == 'POST':
          form = Register(request.POST)
          if form.is_valid():
                 form.save()
                 return HttpResponseRedirect('/login')
   return render(request, 'pages/register.html', {'form' : form})

@login_required
def profile(request):
   return render(request, 'pages/profile.html')

@login_required
def profileupdate(request):
   if request.method == 'POST':
      u_form = UserUpdateForm(request.POST,instance=request.user)
      p_form = ProfileUpdateForm(request.POST, request.FILES,instance=request.user.profile)
      if u_form.is_valid() and p_form.is_valid():
         u_form.save()
         p_form.save()
         return redirect('/profile')
   else:
      u_form = UserUpdateForm(instance=request.user)
      p_form = ProfileUpdateForm(instance=request.user.profile)
   context = {
      'u_form': u_form,
      'p_form': p_form
   }
   return render(request, 'pages/updatep.html',context)

class UserListViews(ListView):
   queryset = User.objects.all()
   template_name = 'pages/user.html'
   context_object_name = 'User'
def destroy(request, id):  
    user = User.objects.get(id=id)  
    user.delete()  
    return redirect("/user")  
def add(request):
   form = AddUserForm()
   if request.method == 'POST':
          form = AddUserForm(request.POST)
          if form.is_valid():
                 form.save()
                 return HttpResponseRedirect('/user')
   return render(request, 'pages/adduser.html', {'form' : form})


         




