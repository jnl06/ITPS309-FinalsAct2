from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisterForm


def register_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created! You can now log in.')
            return redirect('login_user')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            if not request.POST.get('remember_me'):
                request.session.set_expiry(0) 
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})


def logout_user(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('login_user')


@login_required
def dashboard(request):
    stats = [
        {"label": "Total users", "value": "1,284", "change": "12%", "up": True},
        {"label": "Revenue", "value": "$8,430", "change": "4%", "up": True},
        {"label": "Open tickets", "value": "23", "change": "8%", "up": False},
        {"label": "Active today", "value": "312", "change": "2%", "up": True},
    ]
    activity = [
        {"name": "Website redesign", "status": "Done", "date": "Nov 24, 2026"},
        {"name": "Invoice #1042", "status": "Pending", "date": "Nov 23, 2026"},
        {"name": "Email campaign", "status": "Failed", "date": "Nov 22, 2026"},
    ]
    return render(request, 'accounts/dashboard.html',
                  {"stats": stats, "activity": activity})