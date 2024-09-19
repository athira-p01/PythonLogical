import tkinter as tk
from tkinter import *
import pyttsx3

engine = pyttsx3.init()

def speaknow():
    engine.say(textv.get())
    engine.runAndWait()

root = Tk()

textv = StringVar()

obj = LabelFrame(root, text="Text to Speech", font=('Arial', 15), bd=1)
obj.pack(fill="both", expand="yes", padx=10, pady=10)

lbl = Label(obj, text="Text:", font=('Arial', 12))
lbl.pack(side=tk.LEFT, padx=5, pady=5)

text = Entry(obj, textvariable=textv, font=('Arial', 12), width=25, bd=3)
text.pack(side=tk.LEFT, padx=10, pady=5)

btn = Button(obj, text="Speak", font=('Arial', 12), bg="black", fg="white", command=speaknow)
btn.pack(side=tk.LEFT, padx=10, pady=5)

root.title("Text to Speech")
root.geometry("400x150")
root.resizable(False, False)

root.mainloop()
