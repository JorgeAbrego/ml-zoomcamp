import requests

url = 'http://localhost:8080/2015-03-31/functions/function/invocations'

data = {'url': 'https://smithsfruitstores.co.uk/wp-content/uploads/2020/06/baking-potato.jpg'}

result = requests.post(url, json=data).json()
print(result)