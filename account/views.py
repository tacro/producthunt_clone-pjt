from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def signup(request):
    if request.method == 'POST':
        # he wants to signup
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'account/signup.html', {'error': 'Username has already been taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                auth.login(request, user)
                return redirect('home')
        else:
                return render(request, 'account/signup.html', {'error': "Pass doesn't match"})
    else:
        # just access
        return render(request, 'account/signup.html')

def login(request):
    return render(request, 'account/login.html')

def logout(request):
    # TODO Need to route to homepage
    # and don't forget to logout
    return render(request, 'account/logout.html')
