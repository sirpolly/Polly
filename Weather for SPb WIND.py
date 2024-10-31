import requests


def get_weather(city, api_key):
    base_url = (
        f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    )
    response = requests.get(base_url)
    weather_data = response.json()
    return weather_data


def print_weather(weather_data):
    if "main" in weather_data and "temp" in weather_data["main"]:
        temperature_celsius = weather_data["main"]["temp"] - 273.15
        print(f"Temperature: {temperature_celsius:.2f} °C")
    else:
        print("Error: Unable to retrieve temperature data")

    if "name" in weather_data:
        print(f"City: {weather_data['name']}")
    else:
        print("Error: Unable to retrieve city name")

    if "weather" in weather_data and len(weather_data["weather"]) > 0:
        print(f"Weather: {weather_data['weather'][0]['description']}")
    else:
        print("Error: Unable to retrieve weather description")

    if "main" in weather_data and "humidity" in weather_data["main"]:
        print(f"Humidity: {weather_data['main']['humidity']} %")
    else:
        print("Error: Unable to retrieve humidity data")

    if "wind" in weather_data:
        if "speed" in weather_data["wind"]:
            print(f"Wind Speed: {weather_data['wind']['speed']} m/s")
        else:
            print("Error: Unable to retrieve wind speed data")

        if "deg" in weather_data["wind"]:
            wind_deg = weather_data["wind"]["deg"]
            wind_direction = get_wind_direction(wind_deg)
            print(f"Wind Direction: {wind_direction} ({wind_deg}°)")
        else:
            print("Error: Unable to retrieve wind direction data")
    else:
        print("Error: Unable to retrieve wind data")


def get_wind_direction(degree):
    if degree >= 337.5 or degree < 22.5:
        return "North"
    elif 22.5 <= degree < 67.5:
        return "Northeast"
    elif 67.5 <= degree < 112.5:
        return "East"
    elif 112.5 <= degree < 157.5:
        return "Southeast"
    elif 157.5 <= degree < 202.5:
        return "South"
    elif 202.5 <= degree < 247.5:
        return "Southwest"
    elif 247.5 <= degree < 292.5:
        return "West"
    elif 292.5 <= degree < 337.5:
        return "Northwest"


def main():
    api_key = "afb541e1af4ed79ffe4a5d73baf53203"  # Replace with your API key
    city = "Saint Petersburg"  # Set city to Saint Petersburg
    weather_data = get_weather(city, api_key)
    print_weather(weather_data)


if __name__ == "__main__":
    main()
