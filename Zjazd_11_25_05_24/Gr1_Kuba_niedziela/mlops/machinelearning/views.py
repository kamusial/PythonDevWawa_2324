from django.shortcuts import render
from .models import MLModel
from django.views.generic import ListView


# Create your views here.
class MLModelList(ListView):
    model = MLModel
    template_name = 'machinelearning/mlmodel_list.html'

    def get_queryset(self):
        return MLModel.objects.all().order_by('-published')
