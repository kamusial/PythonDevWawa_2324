from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import requests
import json

# Create your views here.


def home_string_based(request):
    return JsonResponse("{ 'key': 'value' }", safe=False)


def home_dict_based(request):
    return JsonResponse(dict({'key': 'value'}))


def home_test(request):
    return JsonResponse(dict({'anotherKey': 'anotherValue'}))


def cats_from_api(request):
    response = requests.get("https://cat-fact.herokuapp.com/facts/")
    json_response = json.loads(response.text)
    return JsonResponse(json_response, safe=False)