import tkinter as tk
from tkinter import ttk, messagebox
import pyttsx3

engine = pyttsx3.init()

def text_to_speech():
    text = text_area.get("1.0", tk.END).strip()
    if not text:
        messagebox.showwarning("Warning", "Please enter text to convert.")
        return

    voice_choice = voice_option.get()
    speed_choice = speed_option.get()

    voices = engine.getProperty('voices')
    if voice_choice == "Male":
        engine.setProperty('voice', voices[0].id)  # Set male voice (default)
    else:
        engine.setProperty('voice', voices[1].id)  # Set female voice

    if speed_choice == "Slow":
        engine.setProperty('rate', 125)  # Slow speed
    elif speed_choice == "Normal":
        engine.setProperty('rate', 200)  # Normal speed
    else:
        engine.setProperty('rate', 300)  # Fast speed

    engine.say(text)
    engine.runAndWait()

root = tk.Tk()
root.title("Text to Speech Converter")
root.geometry("500x500")
root.configure(bg='#1E3D59')

title_label = tk.Label(root, text="TEXT TO SPEECH", font=("Arial", 24), bg='#1E3D59', fg='white')
title_label.pack(pady=10)

text_area = tk.Text(root, height=8, width=50, font=("Arial", 14))
text_area.pack(pady=10)

voice_label = tk.Label(root, text="VOICE", font=("Arial", 12), bg='#1E3D59', fg='white')
voice_label.pack(pady=5)
voice_option = ttk.Combobox(root, values=["Male", "Female"], font=("Arial", 12))
voice_option.set("Male")
voice_option.pack(pady=5)

speed_label = tk.Label(root, text="SPEED", font=("Arial", 12), bg='#1E3D59', fg='white')
speed_label.pack(pady=5)
speed_option = ttk.Combobox(root, values=["Slow", "Normal", "Fast"], font=("Arial", 12))  # Added "Fast"
speed_option.set("Normal")
speed_option.pack(pady=5)

speak_button = tk.Button(root, text="Speak", command=text_to_speech, font=("Arial", 12), bg="#FCA311", fg="white",
                         width=10)
speak_button.pack(pady=10)

root.mainloop()
