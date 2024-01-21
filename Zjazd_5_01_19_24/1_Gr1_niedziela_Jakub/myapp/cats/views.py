from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import requests

# Create your views here.


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

    edited_response = list()
    for i in (0, len(json_response) - 1):
        data_object = json_response[i]
        fields = dict(
            {
                'user': data_object['user'],
                'text': data_object['text'],
                'source': data_object['source'],
                'createdAt': data_object['createdAt'],
                'updatedAt': data_object['updatedAt'],
                'type': data_object['type'],
                'deleted': data_object['deleted'],
                'used': data_object['used']
            }
        )
        edited_response.append(fields)
    return JsonResponse(edited_response, safe=False)

