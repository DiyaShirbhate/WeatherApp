import requests

def get_weather(city):
    API_KEY = "replace_your_api"  # Replace this with your OpenWeatherMap API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    
    if response.status_code == 200:
        print(f"City: {data['name']}")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Weather: {data['weather'][0]['description']}")
    else:
        print("City not found or API error.")

if __name__ == "__main__":
    city_name = input("Enter city name: ")
    get_weather(city_name)
