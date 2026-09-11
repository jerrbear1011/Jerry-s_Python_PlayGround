#AI gen code to understand how to work with APIs 

import requests

def get_weather(city_name, api_key):
    # Base URL for the OpenWeatherMap Current Weather API
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    # Query parameters (using imperial units for Fahrenheit, use 'metric' for Celsius)
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'imperial' 
    }
    
    try:
        # Send the GET request to the API
        response = requests.get(base_url, params=params)
        
        # Raise an exception if the request failed (e.g., 404 or 500 error)
        response.raise_for_status()
        
        # Convert response to a Python dictionary
        weather_data = response.json()
        
        # Extract specific data fields from the JSON payload
        temp = weather_data['main']['temp']
        feels_like = weather_data['main']['feels_like']
        humidity = weather_data['main']['humidity']
        description = weather_data['weather'][0]['description']
        elevation = weather_data['main']['elevation']
        
        # Print the formatted output
        print(f"🌍 Weather in {city_name.title()}:")
        print(f"🌡️  Temperature: {temp}°F")
        print(f"🤔 Feels Like: {feels_like}°F")
        print(f"💧 Humidity: {humidity}%")
        print(f"☁️  Condition: {description.capitalize()}")
        print(f"⛰️  Elevation: {elevation} meters")
    except requests.exceptions.HTTPError:
        print("❌ City not found or invalid API key.")
    except Exception as e:
        print(f"❌ An error occurred: {e}")

# --- Execution ---
if __name__ == "__main__":
    # Replace with your actual OpenWeatherMap API key
    MY_API_KEY = "ae89e011cccfd0d3271d2abbc40fbd30"
    
    city = input("Enter a city name: ")
    get_weather(city, MY_API_KEY)