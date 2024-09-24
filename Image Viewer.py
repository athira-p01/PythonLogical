import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def open_image():
    file_path = filedialog.askopenfilename(
        filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.gif")])

    if file_path:
       img = Image.open(file_path)
       img.thumbnail((400, 400))
       img_tk = ImageTk.PhotoImage(img)
       label.config(image=img_tk)
       label.image = img_tk

def exit_app():
    root.destroy()

root = tk.Tk()
root.title("Image Viewer")
root.geometry("500x500")
button_frame = tk.Frame(root)
button_frame.pack(pady=20)

open_button = tk.Button(button_frame, text="Open Image", command=open_image)
open_button.pack(side=tk.LEFT, padx=10)

exit_button = tk.Button(button_frame, text="Exit", command=exit_app)
exit_button.pack(side=tk.LEFT, padx=10)

label = tk.Label(root)
label.pack(padx=20, pady=20)

root.mainloop()
