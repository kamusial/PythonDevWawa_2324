"""Jak dostać aktualny kurs danej waluty?!!!!!"""
import httpx
from typing import Literal


CURRENCIES = Literal["EUR", "USD", "CHF"]


def get_rate(currency: CURRENCIES, date: str = "last") -> float:
    response = httpx.get(f"https://api.nbp.pl/api/exchangerates/rates/a/{currency}/{date}")
    response_as_dict = response.json()
    return float(response_as_dict["rates"][0]["mid"])


if __name__ == '__main__':
    rate = get_rate("EUR")
    print(rate)
