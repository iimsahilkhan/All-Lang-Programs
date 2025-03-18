import tkinter as tk
from tkinter import ttk
import pyttsx3

def speak():
    text = text_entry.get("1.0", tk.END).strip()
    if text:
        engine.setProperty('rate', speed_var.get())
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[voice_var.get()].id)
        engine.say(text)
        engine.runAndWait()

def clear_text():
    text_entry.delete("1.0", tk.END)

# Initialize TTS engine
engine = pyttsx3.init()

# GUI setup
root = tk.Tk()
root.title("Text to Speech")
root.geometry("400x300")
root.resizable(False, False)

tk.Label(root, text="Enter Text:").pack(pady=5)
text_entry = tk.Text(root, height=5, width=50)
text_entry.pack(pady=5)

# Voice selection
voice_var = tk.IntVar(value=0)
tk.Label(root, text="Select Voice:").pack()
ttk.Radiobutton(root, text="Male", variable=voice_var, value=0).pack()
ttk.Radiobutton(root, text="Female", variable=voice_var, value=1).pack()

# Speed control
speed_var = tk.IntVar(value=150)
tk.Label(root, text="Speech Speed:").pack()
speed_slider = ttk.Scale(root, from_=50, to=300, variable=speed_var, orient='horizontal')
speed_slider.pack()

# Buttons
speak_button = ttk.Button(root, text="Speak", command=speak)
speak_button.pack(pady=5)
clear_button = ttk.Button(root, text="Clear", command=clear_text)
clear_button.pack(pady=5)

root.mainloop()