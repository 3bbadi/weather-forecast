import tkinter as tk
from tkinter import messagebox
import requests

# Function to fetch weather data
def get_weather():
    city = city_entry.get()
    api_key = 'a3035faa212a00d64af14d029ccda97a' 
    base_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

    response = requests.get(base_url)

    if response.status_code == 200:
        data = response.json()
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        pressure = data['main']['pressure']
        precipitation = data.get('rain', {}).get('1h', 0)

        temperature_label.config(text=f"Temperature: {temperature}°C")
        humidity_label.config(text=f"Humidity: {humidity}%")
        wind_speed_label.config(text=f"Wind Speed: {wind_speed} km/h")
        pressure_label.config(text=f"Pressure: {pressure} hPa")
        precipitation_label.config(text=f"Precipitation: {precipitation} mm")
    else:
        messagebox.showerror("Error", "City not found!")

# Initialize tkinter window
app = tk.Tk()
app.title("Weather Forecast")

# GUI elements
tk.Label(app, text="Location:").grid(row=0, column=0, padx=10, pady=10)
city_entry = tk.Entry(app)
city_entry.grid(row=0, column=1, padx=10, pady=10)

search_button = tk.Button(app, text="Search", command=get_weather)
search_button.grid(row=0, column=2, padx=10, pady=10)

temperature_label = tk.Label(app, text="Temperature: ")
temperature_label.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

humidity_label = tk.Label(app, text="Humidity: ")
humidity_label.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

wind_speed_label = tk.Label(app, text="Wind Speed: ")
wind_speed_label.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

pressure_label = tk.Label(app, text="Pressure: ")
pressure_label.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

precipitation_label = tk.Label(app, text="Precipitation: ")
precipitation_label.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

app.mainloop()
