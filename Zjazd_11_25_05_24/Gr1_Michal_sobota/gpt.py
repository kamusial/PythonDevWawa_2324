import click
import httpx

API_KEY = "TU WKLEIĆ WŁASNY KLUCZ"
url = "https://api.edenai.run/v2/text/chat"


def ask(prompt: str) -> str:
    provider = "openai/gpt-3.5-turbo"
    payload = {
        "providers": [provider],
        "text": prompt
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": f"Bearer {API_KEY}"
    }

    response = httpx.post(url, json=payload, headers=headers, timeout=60)
    return response.json()[provider]["generated_text"]


@click.command
@click.argument("prompt")
def main(prompt: str):
    print(ask(prompt))


if __name__ == '__main__':
    main()
