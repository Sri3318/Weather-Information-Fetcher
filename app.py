import tkinter as tk
import requests
from tkinter import messagebox

# OpenWeatherMap API Key
API_KEY = "30d4741c779ba94c470ca1f63045390a"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# Function to determine weather condition
def get_weather_condition(temp_celsius):
    if temp_celsius > 30:
        return "🔥 Hot"
    elif 20 <= temp_celsius <= 30:
        return "⛅ Warm"
    elif 10 <= temp_celsius < 20:
        return "🌥 Cool"
    elif 0 <= temp_celsius < 10:
        return "🌧 Cold"
    else:
        return "❄ Freezing"

# Function to fetch weather data
def get_weather():
    city = city_entry.get().strip()

    if not city:
        messagebox.showwarning("Warning", "Please enter a city name!")
        return

    try:
        params = {"q": city, "appid": API_KEY, "units": "metric"}  # Fetch temperature in Celsius
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if data["cod"] == "404":
            messagebox.showerror("Error", "City not found. Please try again!")
        else:
            weather_main = data["weather"][0]["main"]
            temp_c = round(data["main"]["temp"])  # Celsius
            temp_f = round((temp_c * 9/5) + 32)   # Convert to Fahrenheit
            humidity = data["main"]["humidity"]
            wind_speed = data["wind"]["speed"]
            condition = get_weather_condition(temp_c)

            weather_info = (
                f"City: {city}\n"
                f"Weather: {weather_main} ({condition})\n"
                f"Temperature: {temp_c}°C / {temp_f}°F\n"
                f"Humidity: {humidity}%\n"
                f"Wind Speed: {wind_speed} m/s"
            )

            weather_label.config(text=weather_info)

    except requests.exceptions.RequestException:
        messagebox.showerror("Error", "Failed to fetch weather data. Check your internet connection.")

# Create main application window
app = tk.Tk()
app.title("Weather App")
app.geometry("420x400")
app.config(bg="#242424")

# Title Label
title_label = tk.Label(app, text="🌤 Weather Information", font=("Consolas", 18), bg="#242424", fg="white")
title_label.pack(pady=10)

# City Entry
city_entry = tk.Entry(app, font=("Consolas", 14), width=20)
city_entry.pack(pady=10)

# Search Button
search_button = tk.Button(app, text="Get Weather", font=("Consolas", 14), command=get_weather, bg="blue", fg="white")
search_button.pack(pady=10)

# Weather Info Label
weather_label = tk.Label(app, text="", font=("Consolas", 14), bg="#242424", fg="white", justify="left")
weather_label.pack(pady=10)

# Run the application
app.mainloop()
