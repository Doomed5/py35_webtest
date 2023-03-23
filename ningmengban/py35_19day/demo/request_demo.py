import requests
url = 'http://www.lemon.com/'

response = requests.get(url)
res = response.status_code
# print(res)
# print(response.headers)
# print(response.text)
# print(response.content.decode('utf-8'))
# print(response.json())

print(response.request.headers)
print(response.request.body)