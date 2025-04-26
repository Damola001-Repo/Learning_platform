from django.shortcuts import render, redirect
from .forms import CustomCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.db import IntegrityError
from django.contrib.auth.models import User

# Create your views here.
def userRegistration(request):
    form = CustomCreationForm(request.POST)
    if request.method == 'POST':
        form = CustomCreationForm(request.POST)
        if form.is_valid():
            try:
                user = form.save(commit=False)
                user.username = user.email
                user.save()

                login(request, user)
                messages.success(request, "User Created")
                return redirect('/')
            except IntegrityError:
                messages.error(request, "A user with this email already exists. Click login to log in")
        
    context = {
        'form':form
    }

    return render(request, 'user/registration.html', context)



def userLogin(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('/')
    
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        try:
            user = User.objects.get(email=email)
        except:
            messages.error(request, f"Email {email} does not exist")

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Login Success")
            return redirect('/')
        else:
            messages.error(request, "Email or Password is incorrect")

    context = {
        'page':page
    }

    return render(request, 'user/login.html', context)


def userLogout(request):
    logout(request)
    messages.error(request, 'Logged Out')
    return redirect('/')