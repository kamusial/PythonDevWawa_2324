import httpx
from django.http import JsonResponse, HttpRequest


def api_test_view(request: HttpRequest):
    params = request.GET
    currency = params.get("currency", "EUR")
    date = params.get("date", "")
    response = httpx.get(f"https://api.nbp.pl/api/exchangerates/rates/a/{currency}/{date}")
    stuff_to_show = response.json()["rates"][0]
    return JsonResponse(stuff_to_show)
