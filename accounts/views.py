import pdb
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
from django.shortcuts import render
from .forms import LoginForm, SignUpForm
from .models import Account
from shop.models import Category

categories = Category.objects.all()

def password_similarity_checker(pass_1, pass_2):
    if pass_1 == pass_2:
        return True
    else:
        return False, "Password not similar"



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
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():

            email = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            raw_repeat_password = form.cleaned_data.get('raw_repeat_password')

            if password_similarity_checker(raw_password, raw_repeat_password):

                obj = Account.objects.create(email=email, password=raw_password)
                obj.save()
                send_registration_email(email)

                return redirect('home')
    else:
        print("Invalid form data")
        form = SignUpForm()
    return render(request, 'sign-up.html', {'categories': categories, 'form':form})

def account_settings(request, id):

    return render(request, 'account-settings.html', {'categories': categories})

def account_history(request, id):

    return render(request, 'account-history.html', {'categories': categories})
