from django.shortcuts import render, reverse
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.http.response import HttpResponseRedirect
from django.contrib.auth.models import User

from web.functions import generate_form_errors
from users.forms import CustomerForm


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)

                return HttpResponseRedirect("/")

        context = {
            "title": "Login",
            "error": True,
            "message": "Invalid username or password"
        }
        return render(request, "users/signin.html", context=context)
    else:
        context = {
            "title": "Login"
        }
        return render(request, "users/signin.html", context=context)


def logout(request):
    auth_logout(request)
    return HttpResponseRedirect(reverse("web:index"))


def signup(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            # print(form.cleaned_data)
            form_data = form.cleaned_data
            

            if User.objects.filter(username=form_data['username']):
                form = CustomerForm(instance=instance)
                context = {
                    "title": "Signup",
                    "error": True,
                    "message": "User with username already exists",
                    "form": form,
                }
                return render(request, "users/signup.html", context=context)
            else:
                new_user = User.objects.create_user(
                    username=form_data['username'],
                    password=form_data['password'],
                    email=form_data['email'],
                    first_name=form_data['first_name'],
                    last_name=form_data['last_name']
                )
                instance.user = new_user
                instance.save()         

            user = authenticate(
                request, username=form_data['username'], password=form_data['password'])
            auth_login(request, user)

            return HttpResponseRedirect(reverse("web:index"))

        else:
            message = generate_form_errors(form)

            form = CustomerForm()
            context = {
                "title": "Signup",
                "error": True,
                "message": message,
                "form": form,
            }
            return render(request, "users/signup.html", context=context)

    else:
        form = CustomerForm()
        context = {
            "title": "Signup",
            "form": form,
        }
        return render(request, "users/signup.html", context=context)
