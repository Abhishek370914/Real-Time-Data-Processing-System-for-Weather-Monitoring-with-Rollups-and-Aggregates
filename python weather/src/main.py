from weather_data import get_weather_data
from db_operation import save_weather_data

# main.py or wherever you're using the API key
API_KEY = "703d371d9cbea28726d84206d88e56b3"  # Replace with your actual API key

def main():
    city = "Delhi"  # Change this to any city name
    weather_data = get_weather_data(city, API_KEY)
    
    if weather_data is not None:
        print(f"Weather data for {city}: {weather_data}")
        # Save the data to the database or any storage
        save_weather_data(city, weather_data)
    else:
        print(f"Failed to retrieve weather data for {city}.")

if __name__ == "__main__":
    main()
