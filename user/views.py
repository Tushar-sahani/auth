from django.shortcuts import render,redirect
from . forms import CreateUserForm, LoginForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def index(request):
    return render(request,'user/index.html')


def register(request):
    form = CreateUserForm()

    if request.method == "POST":
        form  = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect("login")
        
    context = {'registerform':form}   
    return render(request,'user/register.html',context=context)


def login(request):

    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request, data = request.POST)

        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username,password=password)

            if user is not None:
                auth.login(request,user)
                return redirect('dashboard',username=username)
    context = {'loginform':form}
    return render(request,'user/login.html',context=context)

@login_required(login_url="login")
def dashboard(request,username):
    context = {"username":username}
    return render(request,'user/dashboard.html',context=context)

def logout(request):
    auth.logout(request)
    
    return redirect("login")

def profile(request):
    data = {
        "username": request.user.username,
        "email": request.user.email,
        # Add more user-related data as needed
    }
    context = {"data": data}
    return render(request, 'user/profile.html', context=context)