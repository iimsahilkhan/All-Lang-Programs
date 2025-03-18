import requests
import json
import tkinter as tk
from tkinter import messagebox

def get_weather():
    city = city_entry.get()
    if not city:
        messagebox.showerror("Error", "Please enter a city name")
        return
        
    try:
        url = f"http://api.weatherapi.com/v1/current.json?key=9fa6955d9c7e433bb7a81707251103&q={city}"
        r = requests.get(url)
        r.raise_for_status()  # Raise an exception for bad status codes
        weather_data = json.loads(r.text)
        temp = weather_data["current"]["temp_c"]
        result_label.config(text=f"Temperature in {city}: {temp}°C")
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Failed to fetch weather data: {str(e)}")
    except (json.JSONDecodeError, KeyError) as e:
        messagebox.showerror("Error", f"Failed to process weather data: {str(e)}")

# Create the main window
root = tk.Tk()
root.title("Weather App")
root.geometry("400x200")
root.configure(padx=20, pady=20)

# Create and pack the city entry field
city_label = tk.Label(root, text="Enter city name:")
city_label.pack(pady=5)
city_entry = tk.Entry(root, width=30)
city_entry.pack(pady=5)

# Create and pack the search button
search_button = tk.Button(root, text="Get Weather", command=get_weather)
search_button.pack(pady=10)

# Create and pack the result label
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

# Start the GUI event loop
root.mainloop()