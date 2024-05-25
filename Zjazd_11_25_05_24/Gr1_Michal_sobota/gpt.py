import click
import httpx
import keyring


url = "https://api.edenai.run/v2/text/chat"


class LoginError(Exception):
    ...


def ask(prompt: str, api_key: str) -> str:
    provider = "openai/gpt-3.5-turbo"
    payload = {
        "providers": [provider],
        "text": prompt
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": f"Bearer {api_key}"
    }

    response = httpx.post(url, json=payload, headers=headers, timeout=60)
    return response.json()[provider]["generated_text"]


@click.group()
def cli():
    ...


@click.command
@click.argument("prompt")
def main_file(prompt: str):
    api_key = open(".eden").read().strip()
    print(ask(prompt, api_key))


@cli.command
@click.argument("prompt")
def main_safe(prompt: str):
    api_key = keyring.get_password("edenAI", "api_key")
    if api_key is None:
        raise LoginError("API key not present in keyring. Run gpt.exe login first.")
    print(ask(prompt, api_key))


@cli.command
@click.argument("api_key")
def login(api_key: str):
    keyring.set_password("edenAI", "api_key", api_key)
    print("API KEY set")


if __name__ == '__main__':
    cli()
