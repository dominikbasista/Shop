import pdb
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
from django.shortcuts import render
from .forms import LoginForm
from shop.models import Category

categories = Category.objects.all()
# pdb.set_trace()
def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(email=cd["email"], password=cd["password"])
            if user is not None:
                login(request, user)
                return HttpResponse("Zalogowano")
            else:
                return HttpResponse("Nieprawidłowe dane")
    else:
        form = LoginForm()
    return render(request, 'login.html', {'categories': categories, 'form': form})

def sign_up(request):
    return render(request, 'sign-up.html', {'categories': categories})

def account_settings(request, id):

    return render(request, 'account-settings.html', {'categories': categories})

def account_history(request, id):

    return render(request, 'account-history.html', {'categories': categories})
