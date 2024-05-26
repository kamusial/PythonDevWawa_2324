from django.shortcuts import render, redirect
from .models import MLModel
from django.views.generic import ListView
from .forms import ModelForm, CategoriseForm
from .model import train_model_and_save_model
from django.http import JsonResponse


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
            train_model_and_save_model(request.user, float(factor), float(noise))
            return redirect("machinelearning:list")
    else:
        form = ModelForm()
    return render(request, "machinelearning/form.html", {'form': form})


def categorise_view(request, pk):
    if request.method == 'POST':
        form = CategoriseForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            x = cd.get('x')
            y = cd.get('y')
            model = MLModel.objects.get(id=pk)
            response = {
                'model': str(model),
                'accuracy': model.accuracy,
                'factor': model.factor,
                'noise': model.noise,
                'author': model.author.username,
                'x': float(x),
                'y': float(y),
                'category': int(model.categorise(float(x), float(y)))
            }
            return JsonResponse(response)
    else:
        form = CategoriseForm()
    return render(request, "machinelearning/form_categorise.html", {'form': form, 'pk': pk})