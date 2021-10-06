import json
import os
import requests

TOKEN = os.environ.get('TOKEN_API')
API = 'https://api.openweathermap.org'
HTTP_HEADERS = {
    'Content-Type': 'application/json'
}


def get(url: str):
    return requests.get(url, headers=HTTP_HEADERS)


def get_current_weather(city: str, args=None):
    url = f'{API}/data/2.5/weather?q={city}&appid={TOKEN}&units=metric'
    return get(url)
