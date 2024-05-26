from django.urls import path
from . import views as mlviews

app_name = 'machinelearning'

urlpatterns = [
    path('', mlviews.MLModelList.as_view(), name='list')
]
