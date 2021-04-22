from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import bcrypt

def index(request):
    return render(request, "index.html")

def register(request):
    errors = User.objects.basic_validator(request.POST)
    if errors:
        for key, value in errors.items():
            messages.error(request, value)
            return redirect('/')

    password = request.POST['password']
    pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

    this_user = User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'], password = pw_hash)
    request.session['user_id'] = this_user.id
    return redirect('/')

def login(request):
        user = User.objects.filter(email=request.POST['email'])
        if user:
            logged_user = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['user_id'] = logged_user.id
            return redirect('/main')

            messages.error(request, "Invalid login")

            return redirect('/')    

def main(request):

        return render(request, "main.html")

def dinning(request):
    return render(request, "dinning.html" )

def add_resteraunt(request):
    return render(request, "resteraunts.html")

def resteraunt_review(request):
    return render(request, "resteraunt_review.html")