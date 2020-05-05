from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from .models import AllLogin
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def gate(request):
    return render(request, 'accounts/gate.html')

def homepage(request):
    return render(request, 'accounts/home.html')

def registration(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('login')
    context = {'form': form}
    return render(request, 'accounts/registration.html', context)

def userlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            AllLogin.objects.create(user=request.user)

            return redirect('homepage')

    return render(request, 'accounts/userlogin.html')

