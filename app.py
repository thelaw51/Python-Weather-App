import requests


apiKey = "a69c642f3e2dd6fb5b142a2fc2b63fed"


userInput = input("Enter city or town: ")

weatherData = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={userInput}&units=metric&APPID={apiKey}")


print(weatherData.json())
