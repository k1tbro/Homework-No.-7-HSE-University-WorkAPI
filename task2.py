import requests

API_KEY = "1e0a3fcc50d3cc0d45348a0e5a4ec952"     

URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city: str) -> None:
    # Параметры запроса
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric",          # температура в °C
        "lang": "ru"                # описание на русском языке
    }
    
    try:
        response = requests.get(URL, params=params)
        response.raise_for_status() 
        
        data = response.json()
        
        # Извлекаем нужные данные
        temp = data["main"]["temp"]
        description = data["weather"][0]["description"]
        city_name = data["name"]
        country = data["sys"]["country"]
        
        print(f"\nПогода в {city_name}, {country}:")
        print(f"Температура: {temp} °C")
        print(f"Описание:    {description.capitalize()}")
        
    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 404:
            print(f"Город '{city}' не найден.")
        else:
            print(f"HTTP ошибка: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Ошибка соединения: {req_err}")
    except KeyError:
        print("Ошибка в формате ответа от сервера.")
    except Exception as e:
        print(f"Неизвестная ошибка: {e}")

if __name__ == "__main__":
    if API_KEY == "":
        print("⚠️  Вставьте свой API-ключ в переменную API_KEY!")
    else:
        city = input("Введите название города: ").strip()
        if city:
            get_weather(city)
        else:
            print("Название города не может быть пустым.")