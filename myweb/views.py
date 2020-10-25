from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth import logout as logout_user
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Create your views here.
def index(req):
	return render(req, 'myweb/index.html')

def drink(req):
	return render(req, 'myweb/Drink.html')

def restaurant(req):
	return render(req, 'myweb/Restaurant.html')

def contact(req):
	return render(req, 'myweb/Contact.html')

def addreviews(req):
	return render(req, 'myweb/Addreviews.html')


def signup(request):
    context = {}
    form = UserCreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('index')
    context['form']=form
    return render(request,'myweb/signup.html',context)

def logout(req):
    logout_user(req)
    return redirect('login')
