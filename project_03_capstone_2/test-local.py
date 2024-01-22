import requests

url = 'http://localhost:8080/2015-03-31/functions/function/invocations'

data = {'text': "I can't believe you made this product, It's the worst I've ever tried."}

result = requests.post(url, json=data).json()
print(result)