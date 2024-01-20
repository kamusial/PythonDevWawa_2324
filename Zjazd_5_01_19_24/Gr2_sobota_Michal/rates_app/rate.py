"""Jak dostać aktualny kurs danej waluty?!!!!!"""
import httpx
import json


response = httpx.get("https://api.nbp.pl/api/exchangerates/rates/a/usd/last")
print(response.text)
response_as_dict = json.loads(response.text)
print(response_as_dict)
