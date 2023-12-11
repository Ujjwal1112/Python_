from django.shortcuts import render, redirect
from django.http import HttpResponse
import users.forms as forms
from users.models import User, Profile
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request, "index.html")

def user_login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        print("email: ", email, "password: ", password)
        check_user = User.objects.filter(email=email)
        if check_user.exists() is False:
            error_message = "Email does not exist"
            messages.error(request, error_message)
            return redirect("login")
        username = check_user[0].username
        valid_user = authenticate(username=username,
                                  password=password)
        if valid_user:
            login(request, valid_user)
            return redirect("profile")
        else:
            error_message = "Invalid email or password"
            messages.error(request, error_message)
            return redirect("login")
    return render(request, "login.html")

def user_register(request):
    register_form = forms.RegisterForm()
    context = {"form": register_form}
    if request.method == "POST":
        form_data = request.POST
        first_name = form_data.get("first_name")
        last_name = form_data.get("last_name")
        email = form_data.get("email")
        password = form_data.get("password")
        confirm_password = form_data.get("confirm_password")
        address = form_data.get("address")
        contact = form_data.get("contact")
        if password != confirm_password:
            error_message = "Passwords does not match!"
            messages.error(request, error_message)
            return redirect("register")
        check_user = User.objects.filter(email=email).exists()
        if check_user is True:
            error_message = "Email is already taken!"
            messages.error(request, error_message)
            return redirect("register")
        # Create user
        user = User.objects.create(first_name=first_name, last_name=last_name, 
                                   email=email, username=email)
        user.set_password(password)  # use this to hash/encrypt the password
        user.save()
        # create profile
        Profile.objects.create(user=user, address=address, contact=contact)
        return redirect("login")
    return render(request, "register.html", context)


@login_required()
def user_profile(request):
    profile = Profile.objects.get(user_id=request.user.pk)
    context = {"profile": profile}
    return render(request, "profile.html", context)



def user_logout(request):
    logout(request)
    return redirect("login")
