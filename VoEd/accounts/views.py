from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from .models import AllLogin
from django.contrib.auth import authenticate, login, logout

# Create0 views.
def gate(request):
    #when the gate view is called, the gate.html will be displayed to users
    return render(request, 'accounts/gate.html')

def homepage(request):
    #when the homepage view is called, the home.html will be displayed to users
    return render(request, 'accounts/home.html')

def registration(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('login')
    context = {'form': form}
    return render(request, 'accounts/registration.html', context)

def userlogin(request):
    # timenow = datetime.datetime.now()
    # print(timenow)
    if request.method == 'POST':
        #get user input of the username and password
        username = request.POST.get('username')
        password = request.POST.get('password')
        #authenticate the user
        user = authenticate(request, username=username, password=password)

        #if the user is authenticated
        if user is not None:
            #call login function and log the user in
            login(request, user)
            #log the timestamp of login into the AllLogin database
            AllLogin.objects.create(user=request.user)

        #render home.html to user by calling the homepage view
            return redirect('homepage')
    #if the user is not authenticated, return to the login page
    return render(request, 'accounts/userlogin.html')

# def userlogout(request):
#     AllLogout.objets.create(user)
#     logout(request)
#
#     return render(request, 'accounts/userlogout.html')