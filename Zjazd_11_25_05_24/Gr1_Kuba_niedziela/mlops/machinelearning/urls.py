from django.urls import path
from . import views as mlviews

app_name = 'machinelearning'

urlpatterns = [
    path('', mlviews.MLModelList.as_view(), name='list'),
    path('train', mlviews.train_view, name='train'),
    path('categorise/<int:pk>', mlviews.categorise_view, name='categorise')
]
