import json
from requests.exceptions import HTTPError
import requests


api_key = 'b00fda0154887b40498b2529a2a72bd3'
city = 'Kiev' 
lang = 'ua' # на українській мові значення
units = 'metric' # температура в цельсіях
api_call = f'http://api.openweathermap.org/data/2.5/find?q={city}&type=like&APPID={api_key}&lang={lang}&units={units}'


def get_weather(api_call):
    try:
        response = requests.get(api_call)

        response.raise_for_status()

        return response.json()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')


if __name__=='__main__':

    weather_data = get_weather(api_call)
    print(weather_data)

    with open('weather_data.json', 'w', encoding='utf-8') as f:
        json.dump(weather_data, f, ensure_ascii=False, indent=3)
