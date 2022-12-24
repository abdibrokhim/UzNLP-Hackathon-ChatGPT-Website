import requests


url = f'http://127.0.0.1:8000/api/'

params = {"question": 'Where is the capital of Russia'}

res = requests.post(url=url, params=params)

print(res.text)
