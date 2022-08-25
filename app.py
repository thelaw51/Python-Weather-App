from cProfile import label
from cgitb import text
import configparser
from distutils.command.config import config
from email import message
from email.mime import image
from tkinter import *
from tkinter import font
from configparser import ConfigParser
from unittest import result
import requests
from tkinter import messagebox



url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&APPID={}"


configFile = "config.ini"
config = ConfigParser()
config.read(configFile)
apiKey = config["api_key"]["key"]


def getWeather(city):
    result = requests.get(url.format(city,apiKey))
    if result.status_code == 200:
        json= result.json()
        city = json["name"]
        country = json["sys"]["country"]
        temp = json["main"]["temp"]
        icon = json["weather"][0]["icon"]
        weather = json["weather"][0]["main"]
        final = (city, country, temp, icon, weather)
        return final
        print(result.status_code)
    else:
        print("error retrivng weather data")
        print(result.status_code)



def search():
    global image
    city = cityText.get()
    Result = getWeather(city)
    if Result:
        lblLocation["text"] = "{},{}".format(Result[0],Result[1])
        img["file"] = 'Icons\\{}.png'.format(Result[3])
        lblTemp["text"] = "{}°".format(Result[2])
        lblWeather["text"] = Result[4]
    else:
        messagebox.showerror("Error","Cannot find city {}".format(city))
    


root = Tk()
root.title("Weather app")
root.geometry("700x350")
root.configure(bg="grey")

cityText = StringVar()
cityEntry = Entry(root,textvariable=cityText,bg="grey")
cityEntry.pack()


btnSearch = Button(root, text="Search weather",width=12, command=search,bg="grey")
btnSearch.pack()


lblLocation = Label(root, text="", font=("raleway thin",20),bg="grey")
lblLocation.pack()

img = PhotoImage(file="")
image=Label(root,image= img,bg="grey")
image.pack()

lblTemp = Label(root, text="",bg="grey")
lblTemp.pack()

lblWeather = Label(root, text="",bg="grey")
lblWeather.pack()

root.mainloop()


































