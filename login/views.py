from django.shortcuts import render,redirect,HttpResponse
# from .models import signup_model
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
         
        if user is not None:
            # Log the user in and redirect to a success page
            login(request, user)
            return redirect('recipes')  # Redirect to the home page or another page
        else:
            # Display an error message if authentication fails
            messages.error(request, "Invalid username or password")
            return redirect('/')
        
    context = {'is_signup': False}
    return render(request, 'login.html', context)

def signup_view(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password1']
        # confermpassword = request.POST['password2']
        
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        
        return redirect('login_view')
    context = {'is_signup': True}
    return render(request, 'login.html', context)
