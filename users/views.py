from django.shortcuts import render, redirect
from django.http import HttpResponse
import users.forms as forms
from users.models import User, Profile
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from products.models import Products
from django.core.paginator import Paginator
from django.db.models import Q
from users.helper import save_image_file_get_url

# Create your views here.


def index(request):
    search = request.GET.get('q')
    sort = request.GET.get('sort', "-created_at")
    all_products = Products.objects.all()
    if search:
        all_products = all_products.filter(Q(specification__icontains = search) | Q(title__icontains=search)) 
    all_products = all_products.order_by(sort)
    page_number = request.GET.get('page')
    pagination = Paginator(all_products, 4)
    pagination_with_data = pagination.get_page(page_number)
    total_pages = list(pagination_with_data.paginator.page_range)
    context = {"pagination_with_data": pagination_with_data, "total_pages": total_pages}
    return render(request, "index.html", context)

def user_login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        check_user = User.objects.filter(email=email) 
        if check_user.exists() is False:
            error_message = "Email does not exist" 
            messages.error(request, error_message)
            return redirect("login")
        username = check_user[0].username
        valid_user = authenticate(username=username,
                                  password=password)
        if valid_user:
            messages.info(request, message='you are logged in')
            login(request, valid_user)
            profile_obj = Profile.objects.get(user_id=request.user.pk)
            request.session["profile_pic"] = profile_obj.profile_picture
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
    AVATAR_URL = "https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-chat/ava3.webp"
    profile = Profile.objects.get(user_id=request.user.pk)
    if profile.profile_picture is None:
        profile.profile_picture = AVATAR_URL
    context = {"profile": profile}
    return render(request, "profile.html", context)



def user_logout(request):
    logout(request)
    return redirect("login")

def new_arrivals(request):
    latest_products = Products.objects.all().order_by("-created_at")[:10]
    product_data = {"lagest_products": latest_products}
    return render(request, "new-arrival.html", product_data)

@login_required
def update_profile(request):
    profile_obj = Profile.objects.get(user_id=request.user.pk)
    if request.method =="POST": 
        address = request.POST.get("address")
        contact = request.POST.get("phone")
        profile_pic = request.FILES.get("profile_pic")
        
        if address and profile_obj.address != address:
            profile_obj.address = address
        
        if contact and profile_obj.contact != contact:
            profile_obj.contact = contact
            
        if profile_pic:
            url = save_image_file_get_url(request, profile_pic)
            print('URL:', url)
            profile_obj.profile_picture = url
        profile_obj.save()
        return redirect('profile')
        
        
        
    


    