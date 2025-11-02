from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import LoginForm


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('products:home')
    return render(request, 'accounts/login.html')


def logout_view(request):
    logout(request)
    return redirect('products:home')

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        User.objects.create_user(username=username, password=password)
        return redirect('accounts:login')
    return render(request, 'accounts/register.html')

def logout_view(request):
    logout(request)
    return redirect('products:home')

def verify_otp(request):
    return render(request, 'accounts/verify_otp.html')


@login_required
def profile(request):
    return render(request, 'accounts/profile.html')



def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('products:home')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect based on user type
            if user.is_superuser:
                return redirect('dashboard:admin_dashboard')
            else:
                return redirect('products:home')
        else:
            messages.error(request, 'Invalid username or password.')
            return render(request, 'accounts/login.html')

    return render(request, 'accounts/login.html')
