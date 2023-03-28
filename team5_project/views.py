from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from . import views


# Create your views here.
def home(request):
    return render(request, "tem5_proj/index.html")


def signup(request):

    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()

        messages.success(request, "Your account is created")

        return redirect("login")


    return render(request, "tem5_proj/signup.html")


def login(request):
    return render(request, "tem5_proj/login.html")


def signout(request):
    pass
