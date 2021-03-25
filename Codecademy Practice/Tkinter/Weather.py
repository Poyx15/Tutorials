import tkinter as tk
import requests

HEIGHT = 600
WIDTH = 800

def test_function(entry):
    print("This is the entry:", entry)


def get_weather(city):
    weather_key = 'a9203b79409d7c444a9c5af73e90be87'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units': 'metric'}
    response = requests.get(url, params=params)
    weather = response.json()

    label['text'] = format_response(weather)


def format_response(weather):
    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']

        final_string = 'City: {name} \n\nDescription: {desc} \nTemperature: {temp} °C'.format(name=name, desc=desc, temp=temp).title()
    except:
        final_string = 'There was a problem \nretrieving that information'

    return final_string

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='landscape.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg="#6699ff", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=40)
entry.place(relx=0, relheight=1, relwidth=0.65)

button = tk.Button(frame, text="Get Weather", command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

lower_frame = tk.Frame(root, bg="#6699ff", bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.60, anchor='n')

label = tk.Label(lower_frame, font=('Courier', 24))
label.place(relheight=1, relwidth=1)

root.mainloop()
