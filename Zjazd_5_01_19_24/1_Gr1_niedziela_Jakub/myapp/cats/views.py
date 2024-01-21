from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.http import HttpResponse, JsonResponse, Http404
import requests
import datetime

# Create your views here.
from .models import CatsFact


def home_string_based(request):
    return JsonResponse("{ 'key': 'value' }", safe=False)


def home_dict_based(request):
    return JsonResponse({'key': 'value'})


def home_test(request):
    return JsonResponse({'anotherKey': 'anotherValue'})


def cats_from_api_old(request):
    response = requests.get("https://cat-fact.herokuapp.com/facts/")
    return JsonResponse(response.json(), safe=False)


def cats_from_api(request):
    response = requests.get("https://cat-fact.herokuapp.com/facts/")
    json_response = response.json()

    wanted_fields = ['user', 'text', 'source', 'createdAt', 'updatedAt', 'type', 'deleted', 'used']
    edited_response = list()
    for i in (0, len(json_response) - 1):
        data_object = json_response[i]
        fields = {key: data_object[key] for key in data_object if key in wanted_fields}
        fields['fact_owner'] = fields.pop('user')
        if CatsFact.objects.count() < 10:
            new_object = CatsFact(**fields)
            new_object.save()
        edited_response.append(fields)
    return JsonResponse(edited_response, safe=False)


def time_now(request):
    return JsonResponse({'time': datetime.datetime.now()})


def xml_view(request):
    return render(request, 'cats/data.xml', content_type='text/xml')


def list_cats_view(request):
    cats = CatsFact.objects.all()
    return render(request, 'list.html', {'cats': cats, 'title': "This is cats list"})


def detail_cats_view(request, pk):
    cat = get_object_or_404(CatsFact, id=pk)
    return render(request, 'detail.html', {'cat': cat, 'title': "This is cat view"})


#from django.shortcuts import redirect
#from django.http import Http404
def detail_cats_view_with_redirect(request, pk):
    try:
        cat = get_object_or_404(CatsFact, id=pk)
    except Http404:
        return redirect('list_cats_view')
    return render(request, 'detail.html', {'cat': cat, 'title': "This is cat view"})