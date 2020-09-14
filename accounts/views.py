from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        print('Username --- {}'.format(username))
        password = request.POST['password']
        print('Password --- {}'.format(password))
        print('User is trying Login ')

        user = auth.authenticate(username=username, password=password)
        print('User --- {}'.format(user))

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now Logged in')
            print("User Logged In")
            print("User Authenticated")
            return redirect('dashboard')
            messages.success(request, "User Authenticated")
        else:
            messages.error(request, 'Invalid Creditentials')
            print("User is having Invalid Creditentials")
            return redirect('login')

    else:
        print("User Came to Log In")
        return render(request, 'accounts/login.html')


@login_required(login_url='/accounts/login/')
def dashboard(request):
    user = User.objects.all()
    return render(request, 'accounts/dashboard.html')


@login_required(login_url='/accounts/login/')
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'Your are now logged out')
        print("User logged out")
    return redirect('index')