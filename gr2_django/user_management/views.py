from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect

from .forms import CreateUserForm, LoginForm


def register(request: HttpRequest) -> HttpResponse:
    context = {"form": CreateUserForm()}
    if request.method == "POST":
        filled_form = CreateUserForm(request.POST)
        if filled_form.is_valid():
            filled_form.save()
            return redirect("login")
        else:
            context["form"] = filled_form

    return render(request, "user_management/register.html", context=context)


def login(request: HttpRequest) -> HttpResponse:
    context = {"form": LoginForm()}
    return render(request, "user_management/login.html", context=context)
