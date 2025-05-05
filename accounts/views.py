from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, login as auth_login
from django.contrib import messages

# Handles user registration using Django's secure built-in form
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Automatically logs in new user after registration
            login(request, user)
            messages.success(request, 'Account created and logged in!')
            return redirect('country_list')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

# Custom login view using Django's AuthenticationForm
def login_view(request):
    if request.user.is_authenticated:
        return redirect('country_list')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Authenticates and starts user session
            user = form.get_user()
            auth_login(request, user)
            messages.success(request, 'Logged in successfully!')
            return redirect('country_list')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

# Go to landing page with redirect if user is already authenticated
def landing(request):
    if request.user.is_authenticated:
        return redirect('country_list')
    return render(request, 'landing.html')
