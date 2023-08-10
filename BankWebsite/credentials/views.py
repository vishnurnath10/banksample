from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
def login(request):
    if request.method=="POST":
        username=request.POST["username"]
        password = request.POST["password"]
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('about')
        else:
            messages.error(request, "invalid credentials")
            return redirect('login')
    return render(request, "login.html")

def logout(request):
    auth.logout(request)
    return redirect('/')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username already exist")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email already exist")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password,first_name=first_name,last_name=last_name, email=email)
                user.save();
                return redirect('login')
        else:
            messages.info(request, 'password not match')
            return redirect('register')
        return render('/')

    return render(request, "register.html")



def form(request):
    if request.method == 'POST':
        message = "Application accepted"
    else:
        message = None

    context = {
        'message': message,
    }
    return render(request, 'form.html', context)

def about(request):
    return render(request, 'about.html')

