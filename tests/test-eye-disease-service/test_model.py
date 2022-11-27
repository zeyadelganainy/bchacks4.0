import requests

BASE = "http://127.0.0.1"
PORT = 5002
ENDPOINT = "/a-eye"

BASE_URL = BASE + ":" + str(PORT)
ENDPOINT_URL = BASE_URL + ENDPOINT


resposne = requests.get(ENDPOINT_URL)
print(resposne.json())
