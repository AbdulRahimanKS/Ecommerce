from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth

# Create your views here.

def register(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('psw')
        password2 = request.POST.get('psw-repeat')
        
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username already exists!")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email id alreadt exists!")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password1, first_name=firstname, last_name=lastname)
                user.save()
                return redirect('/')
        else:
            messages.info(request, "Passwords are not matching!")
            return redirect('register')
    else:
        return render(request, 'register.html') 

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['psw']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "Invalid details")
            return redirect('login')
    else:
        return render(request, "login.html")

def logout(request):
    auth.logout(request)
    return redirect('/')
