from django.shortcuts import render, redirect
from django.contrib import messages
from .import forms

from django.contrib.auth import logout, login, authenticate, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
# Create your views here.


def Register(request):
        if request.method=='POST':
                register_form=forms.RegisterForm(request.POST)
                if register_form.is_valid():
                        messages.success(request, 'user created successful')
                        register_form.save()
                        return redirect('home')
        else:
                register_form=forms.RegisterForm()
        return render(request, 'register.html', {'form':register_form, 'type':'register'})

def user_login(request):
    if request.method=='POST':
        form=AuthenticationForm(request, request.POST)
        if form.is_valid():
            user_name=form.cleaned_data['username']
            user_pass=form.cleaned_data['password']
            user=authenticate(username=user_name, password=user_pass)
            if user is not None:
                messages.success(request, 'Login successfully done')
                login(request, user)
                return redirect('home')
            else:
                messages.warning(request, 'user do not find please  login')
                return  redirect('register')
          
    else:
        form=AuthenticationForm()
        return render(request, 'register.html', {'form':form, 'type':'login'})

def user_logout(request):
        logout(request)
        return redirect('register')



def pass_change(request):
        if request.user.is_authenticated:
                if request.method == 'POST':
                        form = PasswordChangeForm(user=request.user, data=request.POST)
                        if form.is_valid():
                                form.save()
                                update_session_auth_hash(request, form.user)  # Use form.user directly
                                return redirect('profile')
                else:
                        form = PasswordChangeForm(user=request.user)
                return render(request, 'pass_change.html', {'form': form})
        else:
              return redirect('login')   
      
def pass_change2(request):
        if request.user.is_authenticated:
                if request.method == 'POST':
                        form = SetPasswordForm(user=request.user, data=request.POST)
                        if form.is_valid():
                                form.save()
                                update_session_auth_hash(request, form.user)  # Use form.user directly
                                return redirect('profile')
                else:
                        form = SetPasswordForm(user=request.user)
                return render(request, 'pass_change.html', {'form': form})
        else:
              return redirect('login')   
      
   