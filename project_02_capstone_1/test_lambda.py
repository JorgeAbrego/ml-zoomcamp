import requests

url = 'https://7wep8lbmz1.execute-api.us-east-1.amazonaws.com/test/predict'

data = {'url': 'https://smithsfruitstores.co.uk/wp-content/uploads/2020/06/baking-potato.jpg'}

result = requests.post(url, json=data).json()
print(result)