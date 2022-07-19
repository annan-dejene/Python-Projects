import requests


# API Key provided by openweathermap.org to fetch wether data
API_KEY = 'd01b273d7cc1a73855e86c432fc39b97'


def coordinate_from_city(city_name, API_KEY):
    params = {'q': city_name, 'appid': API_KEY}
    url = 'http://api.openweathermap.org/geo/1.0/direct'
    r = requests.get(url=url, params=params)
    if r.status_code == 200:
        json_data = r.json()[0]
        return json_data['lat'], json_data['lon']
    else:
        print(f"Error! Status Code: {r.status_code}")
        exit()


city = input('Enter your city: ')
(lat, lon) = coordinate_from_city(city_name=city, API_KEY=API_KEY)

params = {'lat': lat, 'lon': lon, 'appid': API_KEY, 'units': 'metric'}
url = 'https://api.openweathermap.org/data/2.5/weather'

respons = requests.get(url=url, params=params)
if respons.status_code == 200:
    json_response = respons.json()
    weather_description = json_response['weather'][0]['description'].title()
    tempreture = json_response['main']['temp']
    pressure = json_response['main']['pressure']
    humidity = json_response['main']['humidity']
    wind_speed = json_response['wind']['speed']
else:
    print(f"Error! Status Code: {respons.status_code}")
    exit()
