from django.urls import path,include
from django.contrib.auth import views as aunt_views
from . import views

urlpatterns = [
    path('', aunt_views.LoginView.as_view(template_name='myweb/login.html'), name='login'),
    path('signup', views.signup, name='signup'),
    path('index', views.index, name='index'),
    path('logout', views.logout, name='logout'),
    path('restaurant', views.restaurant, name='restaurant'),
    path('drink', views.drink, name='drink'),
    path('contact', views.contact, name='Contact'),
    path('addreviews', views.addreviews, name='addreviews'),
]