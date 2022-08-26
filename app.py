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
        lblLocation.pack()
        image.pack()
        lblTemp.pack()
        lblWeather.pack()
        return final
        print(result.status_code)
    else:
        print("error retrivng weather data")
        print(result.status_code)



def search(event):
    global image
    city = cityText.get()
    Result = getWeather(city)
    if Result:
        lblLocation["text"] = "{},{}".format(Result[0],Result[1])
        img["file"] = 'Icons\\{}.png'.format(Result[3])
        lblTemp["text"] = "{}°".format(Result[2])
        lblWeather["text"] = Result[4]
        cityEntry.place(rely=0.6)

    else:
        messagebox.showerror("Error","Cannot find city {}".format(city))
    


root = Tk()
root.title("Weather app")
root.geometry("700x350")
root.configure(bg="grey")
root.resizable(0,0)

cityText = StringVar()
cityEntry = Entry(root,textvariable=cityText,bg="grey")
cityEntry.place(relx=0.5,rely=0.4,anchor=CENTER)
cityEntry.insert(0,"Enter city or town")
cityEntry.bind("<Return>",search)

lblLocation = Label(root, text="", font=("raleway thin",20),bg="grey")


img = PhotoImage(file="")
image=Label(root,image= img,bg="grey")


lblTemp = Label(root, text="",bg="grey")


lblWeather = Label(root, text="",bg="grey")


root.mainloop()


































