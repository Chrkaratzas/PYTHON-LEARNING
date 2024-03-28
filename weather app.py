import tkinter as tk
from tkinter import ttk, PhotoImage
import requests
from PIL import Image, ImageTk


# Function to convert Kelvin to Celsius
def kelvin_to_celsius(kelvin):
    return int(kelvin - 273.15)


# Function to fetch weather data
def fetch_weather():
    user_city_input = city_entry.get()
    url = BASE_URL + "appid=" + api_key + "&q=" + user_city_input
    response = requests.get(url).json()

    kelvin_temp = response['main']['temp']
    temp_celsius = kelvin_to_celsius(kelvin_temp)
    weather = response['weather'][0]['main']

    # Update labels with the weather and temperature
    weather_label.config(text=f"Weather: {weather}")
    temp_label.config(text=f"Temperature: {temp_celsius}°C")

    # Update image based on temperature
    if temp_celsius > 25:
        img = Image.open(hot_image_path)
    elif temp_celsius < 10:
        img = Image.open(cold_image_path)
    else:
        img = Image.open(default_image_path)

    img = img.resize((100, 100), Image.Resampling.LANCZOS)
    photo = ImageTk.PhotoImage(img)
    image_label.config(image=photo)
    image_label.image = photo  # keep a reference!


# Main application window
app = tk.Tk()
app.title("Weather App")

# Global variables
api_key = '08716b961654ee4661fc8de60de9c09b'
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

hot_image_path = 'hot_sun.png'
cold_image_path = 'cold.png'
default_image_path = 'sun-and-clouds-sticker.jpg'

# UI Components
city_entry = ttk.Entry(app)
city_entry.pack(pady=10)

fetch_weather_button = ttk.Button(app, text="Get Weather", command=fetch_weather)
fetch_weather_button.pack(pady=5)

weather_label = ttk.Label(app, text="Weather: ")
weather_label.pack(pady=5)

temp_label = ttk.Label(app, text="Temperature: ")
temp_label.pack(pady=5)

image_label = ttk.Label(app)
image_label.pack(pady=10)

# Start the application
app.mainloop()
