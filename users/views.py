from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from . import forms, models

# Create your views here.
def register_view(request):
    if request.method =='POST':
        form = forms.RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = forms.RegistrationForm()
    
    return render(request, 'users/register.html', {'form':form})


def login_view(request):
    # if request.user.is_authenticated:
    #     return redirect('home')

    if request.method == "POST":
        form = forms.LoginForm(request.POST, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
        
            return redirect('home')
    else:
        form = forms.LoginForm()
    
    return render(request, 'users/login.html', {'form':form})


@login_required
def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def profile_update_view(request):
    try:
        profile = request.user.profile
    except models.Profile.DoesNotExist:
        profile = models.Profile.objects.create(user=request.user)

    if request.method == "POST":
        form =forms.ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = forms.ProfileForm(instance=profile)

    return render(request, 'users/profile_update.html', {'form':form})