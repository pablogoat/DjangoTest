from django.shortcuts import render, redirect
from .forms import RegisterForm

# Create your views here.

def register(response): 
    if response.method == "POST": #saving new account
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()

        return redirect('/home')
    else:   #creating account creation form
        form = RegisterForm()

    
    return render(response, "register/reg_page.html", {"form": form})