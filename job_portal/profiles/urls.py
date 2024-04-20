# profiles/urls.py
from django.urls import path
from . import views
from .views import register, registration_success
from .views import user_login



urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('register/', views.register, name='register'),
    path('profile/', views.create_profile, name='profile'),
    path('register/', register, name='register'),
    path('registration-success/', registration_success, name='registration_success'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.logout_view, name='logout'),  # Add this line for logout
    path('new-homepage/', views.new_homepage, name='new_homepage'),
    path('generate-pdf/', views.generate_pdf, name='generate_pdf'),
    path('create/', views.create_profile, name='create_profile'),  # Correctly pointing to create_profile view


]
