from django.shortcuts import render

from .forms import NameForm, CrispyNameForm


def form1(request):
    context = {}
    if request.method == "POST":
        first_name = request.POST.get("first-name")
        surname = request.POST.get("last-name")
        context = {
            "first_name": first_name,
            "last_name": surname
        }
    return render(request, "form1.html", context=context)


def form2(request):
    form = NameForm()
    context = {
        "form": form
    }
    if request.method == "POST":
        filled_form = NameForm(request.POST)
        if filled_form.is_valid():
            context = {
                "form": form,
                "first_name": filled_form.cleaned_data.get("first_name"),
                "last_name": filled_form.cleaned_data.get("last_name")
            }
        else:
            context["form"] = filled_form
    return render(request, "form2.html", context=context)


def form3(request):
    form = CrispyNameForm()
    context = {
        "form": form
    }
    if request.method == "POST":
        filled_form = CrispyNameForm(request.POST)
        if filled_form.is_valid():
            context = {
                "form": form,
                "first_name": filled_form.cleaned_data.get("first_name"),
                "last_name": filled_form.cleaned_data.get("last_name")
            }
        else:
            context["form"] = filled_form
    return render(request, "form3.html", context=context)
