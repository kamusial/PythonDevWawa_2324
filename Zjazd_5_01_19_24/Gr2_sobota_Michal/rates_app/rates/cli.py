import click

from .rate import get_rate, CURRENCIES


@click.command()
@click.argument("currency")
def main(currency: CURRENCIES):
    rate = get_rate(currency)
    print(rate)
