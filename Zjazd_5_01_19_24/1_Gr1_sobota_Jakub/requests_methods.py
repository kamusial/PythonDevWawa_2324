import requests

"""
print(r.text)
print(r.status_code)
print(r.headers)
print(r.content)
"""
"""
r = requests.get('https://httpbin.org/get')
r = requests.put('https://httpbin.org/put', data={'key': 'value'})
r = requests.delete('https://httpbin.org/delete')
r = requests.head('https://httpbin.org/get')
"""
import json

x = """{"Date": "Sat, 20 Jan 2024 08:02:32 GMT", "Any": "Other field"}"""

y = json.loads(x)

#print(y)

response = requests.get("https://cat-fact.herokuapp.com/facts/")

json_response = json.loads(response.text)

print(response.text)
print(json_response)
print(json_response[0])
print(json_response[0]['status'])
print(json_response[0]['status']['sentCount'])

#print(json_response[0]['user'])


for i in (0, len(json_response) - 1):
    print(json_response[i]['text'])

text_list = [json_response[i]['text'] for i in (0, len(json_response) - 1)]
print(text_list)