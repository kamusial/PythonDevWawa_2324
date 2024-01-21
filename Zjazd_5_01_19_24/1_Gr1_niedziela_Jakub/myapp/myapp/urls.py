"""
URL configuration for myapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from cats import views as cats_views

urlpatterns = [
    path('', cats_views.home_dict_based, name='home'),
    path('cats/', cats_views.cats_from_api, name='cats_from_api'),
    path('all_cats/', cats_views.list_cats_view, name='list_cats_view'),
    path('cats/<int:pk>/', cats_views.detail_cats_view, name='detail_cats_view'),
    path('xml/', cats_views.xml_view, name='xml_view'),
    path('time/', cats_views.time_now, name='time_now'),
    path('test/', cats_views.home_test, name='home_test'),
    path('admin/', admin.site.urls),
]
