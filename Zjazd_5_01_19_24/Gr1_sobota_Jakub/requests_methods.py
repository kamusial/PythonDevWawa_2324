import requests

"""
print(r.text)
print(r.status_code)
print(r.headers)
print(r.content)
"""

r = requests.get('https://httpbin.org/get')
r = requests.put('https://httpbin.org/put', data={'key': 'value'})
r = requests.delete('https://httpbin.org/delete')
r = requests.head('https://httpbin.org/get')

import json

x = """{"Date": "Sat, 20 Jan 2024 08:02:32 GMT", "Any": "Other field"}"""

y = json.loads(x)

print(y)
