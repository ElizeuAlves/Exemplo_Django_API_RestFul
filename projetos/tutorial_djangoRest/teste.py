import requests
import json


data = {}

data = requests.get("http://127.0.0.1:8000/snippets/")

data = data.json()

for k in data:
	for c, v in k.items():
		print(c, v)