import tkinter as tk
from tkinter import messagebox

# Create the main window
root = tk.Tk()
root.title("Calculator")
root.geometry("400x400")
root.configure(padx=20, pady=20)

# Create and pack the city entry field
city_label = tk.Label(root, text="Enter city name:")
city_label.pack(pady=5)
city_entry = tk.Entry(root, width=30)
city_entry.pack(pady=5)

# Create and pack the search button
search_button = tk.Button(root, text="Get Weather")
search_button.pack(pady=10)

# Create and pack the result label
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

# Start the GUI event loop
root.mainloop()
