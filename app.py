import requests


apiKey = "a69c642f3e2dd6fb5b142a2fc2b63fed"


userInput = input("Enter city or town: ")

weatherData = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={userInput}&units=metric&APPID={apiKey}")

weather = weatherData.json()['weather'][0]['main']
temp =round(weatherData.json()['main']['temp'])

print(f"The weather in {userInput} is: {weather}")
print(f"The temperature in {userInput} is: {temp}°C")
print(f"api call return code: {weatherData.status_code}")

