from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import requests

# Create your views here.
from .models import CatsFact


def home_string_based(request):
    return JsonResponse("{ 'key': 'value' }", safe=False)


def home_dict_based(request):
    return JsonResponse(dict({'key': 'value'}))


def home_test(request):
    return JsonResponse(dict({'anotherKey': 'anotherValue'}))


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

