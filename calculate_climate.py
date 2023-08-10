from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import messagebox
from timezonefinder import TimezoneFinder
import pytz
from datetime import datetime
import requests


def calculate_climate():
    try:
        city = textfield.get()
        geolocator = Nominatim(user_agent="geoapiExercises")
        location = geolocator.geocode(city)
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%I:%M %p")
        clock.config(text=current_time)

        api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=646824f2b7b86caffec1d0b16ea77f79"

        json_data = requests.get(api).json()
        description = json_data['weather'][0]['description']
        temp = int(json_data['main']['temp']-273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']

        t.config(text=(temp, "°C"))

        w.config(text=wind)
        h.config(text=humidity)
        d.config(text=description)
        p.config(text=pressure)
        name.config(text=city)
    except Exception as e:
        messagebox.showerror("Climate Climbers", "Invalid Entry, Please Enter Your Text Correctly And With The Correct Spelling. please kindly try to check your internet connection.")

root = Tk()
root.geometry("1000x600+350+100")
root.config(bg="#1ae5ef")
root.resizable(FALSE, FALSE)
root.title("The Climate Calculator")

# main icon of the image
photo_icon = PhotoImage(file='images/logo.png')
root.iconphoto(False, photo_icon)

# search space
search_image = PhotoImage(file="images/search space.PNG")
myimage = Label(image=search_image, bg="grey")
myimage.place(x=30, y=27, width=280, height=70)

# the text field
textfield = tk.Entry(root, justify="center", width=10, font=("poppins", 25, "bold"), bg="green", border=9, fg="white")
textfield.place(x=38, y=33)
textfield.focus()

# search icon image
search_icon_image = PhotoImage(file="images/search.PNG")
myimage_icon = Button(image=search_icon_image, borderwidth=0, cursor="hand2", command=calculate_climate)
myimage_icon.place(x=252, y=40)

# creating city name display
Label(root, text="The Climate Calculator", font=("algerian", 35, "bold"), bg="#1ae5ef", fg="purple").place(x=320, y=30)

name = Label(root, text="", font=("algerian", 50, "bold"), bg="#1ae5ef", fg="red")
name.place(x=70, y=132)

# temperature
t = Label( text="", font=("arial", 55), fg="blue", bg="#1ae5ef")
t.place(x=70, y=225)
clock = Label(root, text="", font=("helvetica", 25), bg="#1ae5ef", fg="black")
clock.place(x=300, y=240)

# packing the bottom area
frame = Frame(root, width=1020, height=250, bg="#212120")
frame.pack(side=BOTTOM)

# showing the box
First_Box = PhotoImage(file="images/box.PNG")

Label(frame, image=First_Box, bg="#212120").place(x=15, y=20)
Label(frame, image=First_Box, bg="#212120").place(x=275, y=20)
Label(frame, image=First_Box, bg="#212120").place(x=555, y=20)
Label(frame, image=First_Box, bg="#212120").place(x=840, y=20)

# wind
label1 = Label(frame, text="WIND", font=("helvetica", 15, "bold"), fg="White", bg="black")
label1.place(x=60, y=30)

# humidity
label1 = Label(frame, text="HUMIDITY", font=("helvetica", 15, "bold"), fg="White", bg="black")
label1.place(x=300, y=30)

# description
label1 = Label(frame, text="DESCRIPTION", font=("helvetica", 15, "bold"), fg="White", bg="black")
label1.place(x=560, y=30)

# pressure
label1 = Label(frame, text="PRESSURE", font=("helvetica", 15, "bold"), fg="White", bg="black")
label1.place(x=860, y=30)


w = Label(text="", font=("arial", 15, "bold"), fg="white", bg="black")
w.place(x=60, y=460)
h = Label(text="", font=("arial", 15, "bold"), fg="white", bg="black")
h.place(x=300, y=460)
d = Label(text="", font=("arial", 15, "bold"), fg="white", bg="black")
d.place(x=560, y=460)
p = Label(text="", font=("arial", 15, "bold"), fg="white", bg="black")
p.place(x=860, y=460)

root.mainloop()
