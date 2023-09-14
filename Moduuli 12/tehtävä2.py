import requests
def kelvin_to_celsius(kelvin):
    return kelvin - 273.15  # Kelvin to Celsius conversion formula

api_key = "da3a7df90e87c269d5e1f792410788f3"

paikkakunta = input("Syötä paikkakunnan nimi: ")

url = f"http://api.openweathermap.org/data/2.5/weather?q={paikkakunta}&appid={api_key}"

try:
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        sää = data["weather"][0]["description"]
        lämpötila_k = data["main"]["temp"]
        lämpötila_c = kelvin_to_celsius(lämpötila_k)

        print(f"Sää paikkakunnalla {paikkakunta}: {sää}")
        print(f"Lämpötila: {lämpötila_c:.2f} °C")
    else:
        print("Säätilan haku epäonnistui.")
except requests.exceptions.RequestException as e:
    print("Säätilan haku epäonnistui.")
