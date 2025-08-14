import requests
import tkinter as tk
from tkinter import messagebox

# API details
API_KEY = "b67808376a5de016877f3955b7acb505"  # Replace with your OpenWeatherMap API key
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# Function to determine weather emoji based on weather ID
def get_weather_emoji(weather_id):
    if 200 <= weather_id <= 232:
        return "⛈"
    elif 300 <= weather_id <= 321:
        return "🌦"
    elif 500 <= weather_id <= 531:
        return "🌧"
    elif 600 <= weather_id <= 622:
        return "❄"
    elif 701 <= weather_id <= 741:
        return "🌫"
    elif weather_id == 762:
        return "🌋"
    elif weather_id == 771:
        return "💨"
    elif weather_id == 781:
        return "🌪"
    elif weather_id == 800:
        return "☀"
    elif 801 <= weather_id <= 804:
        return "☁"
    else:
        return "🌈"

# Function to get weather
def get_weather():
    city = city_entry.get().strip()
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name")
        return

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"  # Celsius
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        if data["cod"] == 200:
            main = data["main"]
            wind = data["wind"]
            weather = data["weather"][0]
            weather_id = weather["id"]
            description = weather["description"]

            emoji = get_weather_emoji(weather_id)
            temp = main["temp"]
            feels_like = main["feels_like"]
            humidity = main["humidity"]
            wind_speed = wind["speed"]

            temperature_label.config(text=f"{temp:.1f}°C")
            emoji_label.config(text=emoji)
            description_label.config(text=description.capitalize())
            details_label.config(text=f"Feels Like: {feels_like:.1f}°C\nHumidity: {humidity}%\nWind: {wind_speed} m/s")
        else:
            messagebox.showerror("Error", "City not found or API error!")
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# GUI setup
root = tk.Tk()
root.title("🌤 Weather App")

# Desired window size
window_width = 400
window_height = 400

# Center the window
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)
root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")
root.config(bg="#87CEEB")  # Sky blue background

# Title
title_label = tk.Label(root, text="🌤 Weather App", font=("Helvetica", 20, "bold"), bg="#87CEEB", fg="white")
title_label.pack(pady=15)

# Entry and Button Frame
input_frame = tk.Frame(root, bg="#87CEEB")
input_frame.pack(pady=10)

city_entry = tk.Entry(input_frame, font=("Arial", 14), justify="center", width=15)
city_entry.pack(side="left", padx=5)
get_button = tk.Button(input_frame, text="Get Weather", font=("Arial", 12, "bold"), bg="#00796b", fg="white", command=get_weather)
get_button.pack(side="left", padx=5)

# Weather Display
temperature_label = tk.Label(root, text="", font=("Arial", 50, "bold"), bg="#87CEEB")
temperature_label.pack(pady=5)
emoji_label = tk.Label(root, text="", font=("Segoe UI Emoji", 60), bg="#87CEEB")
emoji_label.pack(pady=5)
description_label = tk.Label(root, text="", font=("Arial", 20), bg="#87CEEB")
description_label.pack(pady=5)
details_label = tk.Label(root, text="", font=("Arial", 14), bg="#87CEEB", justify="center")
details_label.pack(pady=5)

# Run the app
root.mainloop()
