import requests

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

import requests

def get_weather_data(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: Failed to retrieve data. Status code: {response.status_code}")
        print(response.json())  # This will show the error message from the API
        return None

    data = response.json()

    # Check if 'main' exists in the response
    if 'main' in data:
        weather_data = {
            "temp": kelvin_to_celsius(data['main']['temp']),
            "feels_like": kelvin_to_celsius(data['main']['feels_like']),
            "main": data['weather'][0]['main'],
            "timestamp": data['dt']
        }
        return weather_data
    else:
        print("Error: 'main' key is missing from the API response.")
        print(data)  # Print the full response for debugging
        return None
