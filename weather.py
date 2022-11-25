from urllib import response
from black import main
from qtpy import API
import requests

API_KEY = "8fbebd999b911d22f5b10e355d5a072e"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("enter a city name : ")
requests_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(requests_url)

if response.status_code == 200:
    data= response.json()
    weather = data["weather"][0]["description"]
    print(weather)
    temperature = data["main"]["temp"] - 273
    print(temperature)
else:
    print("hata !!")