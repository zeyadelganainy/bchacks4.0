import requests

BASE = "http://127.0.0.1"
PORT = 5001
ENDPOINT = "/skin-cancer"

BASE_URL = BASE + ":" + str(PORT)
ENDPOINT_URL = BASE_URL + ENDPOINT


resposne = requests.get(ENDPOINT_URL)
print(resposne.json())
