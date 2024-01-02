from django.shortcuts import render,redirect
from . forms import CreateUserForm
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
    return render(request,'user/login.html')

def dashboard(request):
    return render(request,'user/dashboard.html')