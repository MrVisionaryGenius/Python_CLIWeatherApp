import requests
import json
import math

# API key and URL
api_key = "30d4741c779ba94c470ca1f63045390a"
url = "http://api.openweathermap.org/data/2.5/weather"


# developing a function to fetch the weather data
def get_weather_data(city):
    params = {
        "q": city,
        "appid": api_key,
        "units": "imperial"
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()

def display_weather_data(data):
    print(f"Weather data for {data['name']}:")
    temp_feh = data['main']['temp']
    fehrenheit_to_celsius(temp_feh)
    print(f"Weather: {data['weather'][0]['description']}")
    print(f"Wind Speed: {data['wind']['speed']} km/h")

#Developing a function to convert the temperature from fehrenheit to celsius
def fehrenheit_to_celsius(temp_feh):
    temp_cel = (temp_feh - 32) * 5/9
    print(f"Temperature: {math.ceil(temp_cel)}°C")

def get_city():
    city = input("Enter the city name: ")
    return city.strip().lower()

def main():
    try:
        city = get_city()
        data = get_weather_data(city)
        display_weather_data(data)
    except requests.exceptions.HTTPError as err:
        print("Http Error",err)
    except requests.exceptions.RequestException as err:
        print("Request Error",err)
    except (KeyError, IndexError) as err:
        print("Typing Error",err)
    except Exception as err:
        print(err)

if __name__ == "__main__":
    main()