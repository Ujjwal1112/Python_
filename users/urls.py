from django.urls import path
import users.views as user_views

urlpatterns = [
    path("", user_views.index, name="index"),
    path("login", user_views.user_login, name="login"),
    path("register", user_views.user_register, name="register"),
    path("profile", user_views.user_profile, name="profile"),
    path("logout", user_views.user_logout, name="logout"),
    path("new-arrival", user_views.new_arrivals, name="new-arrival")
]       