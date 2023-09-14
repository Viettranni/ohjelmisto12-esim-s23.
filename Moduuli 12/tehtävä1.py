import requests

pyyntö = "https://api.chucknorris.io/jokes/random"

try:
    vastaus = requests.get(pyyntö)
    if vastaus.status_code == 200:
        json_vastaus = vastaus.json()
        joke = json_vastaus["value"]
        print(joke)
    else:
        print("Hakua ei suoritettu onnistuneesti.")
except requests.exceptions.RequestException as e:
    print ("Hakua ei voitu suorittaa.")
