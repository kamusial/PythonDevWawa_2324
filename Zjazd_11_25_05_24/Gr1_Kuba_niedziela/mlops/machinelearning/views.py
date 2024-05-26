from django.shortcuts import render, redirect
from .models import MLModel
from django.views.generic import ListView
from .forms import ModelForm, CategoriseForm
from .model import train_model


# Create your views here.
class MLModelList(ListView):
    model = MLModel
    template_name = 'machinelearning/mlmodel_list.html'

    def get_queryset(self):
        return MLModel.objects.all().order_by('-published')


def train_view(request):
    if request.method == 'POST':
        form = ModelForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            factor = cd.get('factor')
            noise = cd.get('noise')
            train_model(float(factor), float(noise))
            return redirect("machinelearning:list")
    else:
        form = ModelForm()
    return render(request, "machinelearning/form.html", {'form': form})
