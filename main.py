import requests

def get_weather(city, api_key):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key}

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            weather = data["weather"][0]["description"]
            temp_kelvin = data["main"]["temp"]
            temp_celsius = temp_kelvin - 273.15

            print(f"Hava Durumu: {weather}")
            print(f"Sıcaklık: {temp_celsius:.2f} °C")
        else:
            print("Hava durumu bilgisi alınamadı.")

    except requests.exceptions.RequestException as e:
        print(f"Hata: {e}")

if __name__ == "__main__":
    city_name = input("Hangi şehir için hava durumu öğrenmek istiyorsunuz? ")
    api_key = "YOUR_API_KEY"  # OpenWeatherMap'ten alınan API anahtarı buraya yazılmalıdır.
    get_weather(city_name, api_key)
