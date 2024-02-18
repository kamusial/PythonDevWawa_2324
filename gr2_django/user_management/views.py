from django.shortcuts import render
from .forms import CreateUserForm


def register(request):
    context = {"form": CreateUserForm()}
    return render(request, "user_management/register.html", context=context)
