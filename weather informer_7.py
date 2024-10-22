import requests

def get_weather(city, api_key):
    print("Отправка запроса к API OpenWeatherMap...")
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        response = requests.get(base_url)
        print("Ответ от API OpenWeatherMap:", response.status_code, response.reason)
        response.raise_for_status()
        weather_data = response.json()
        return weather_data
    except requests.exceptions.RequestException as e:
        print("Ошибка запроса:", e)
        return None

def print_weather(weather_data):
    print("Вывод данных о погоде...")
    if weather_data is None:
        print("Ошибка: не удалось получить данные о погоде")
        return

    try:
        temperature = weather_data['main']['temp']
        description = weather_data['weather'][0]['description']
        humidity = weather_data['main']['humidity']
        wind_speed = weather_data['wind']['speed']
        pressure = weather_data['main']['pressure']

        print(f"Температура: {temperature}°C")
        print(f"Описание: {description}")
        print(f"Влажность: {humidity}%")
        print(f"Скорость ветра: {wind_speed} м/с")
        print(f"Атмосферное давление: {pressure} гПа")
    except KeyError as e:
        print(f"Ошибка обработки данных: отсутствует ключ {e}")

def main():
    api_key = "afb541e1af4ed79ffe4a5d73baf53203"  # Вставьте свой API ключ здесь!
    city = input("Введите название города: ")
    while not city.strip():
        print("Ошибка: название города не может быть пустым")
        city = input("Введите название города: ")

    print("Получение данных о погоде для города", city)
    weather_data = get_weather(city, api_key)
    print("Данные о погоде получены:", weather_data)
    print_weather(weather_data)

if __name__ == "__main__":
    main()
