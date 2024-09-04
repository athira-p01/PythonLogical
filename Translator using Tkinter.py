import tkinter as tk
from tkinter import ttk
from tkinter import Canvas
from googletrans import Translator, LANGUAGES

# Prepare language data
languages = list(LANGUAGES.values())
lang_codes = list(LANGUAGES.keys())

# Function to translate text
def translate_text():
    translator = Translator()
    source_text = text_input.get("1.0", "end-1c")
    src_lang = lang_codes[languages.index(source_lang.get())]
    dest_lang = lang_codes[languages.index(target_lang.get())]
    translation = translator.translate(source_text, src=src_lang, dest=dest_lang)
    text_output.delete("1.0", "end")
    text_output.insert("end", translation.text)

# Function to create a gradient background
def create_gradient(canvas, color1, color2):
    steps = 100
    for i in range(steps):
        color = canvas.winfo_rgb(color1)
        r1, g1, b1 = [int(x / 256) for x in color]
        color = canvas.winfo_rgb(color2)
        r2, g2, b2 = [int(x / 256) for x in color]
        r = r1 + (r2 - r1) * i // steps
        g = g1 + (g2 - g1) * i // steps
        b = b1 + (b2 - b1) * i // steps
        color = f'#{r:02x}{g:02x}{b:02x}'
        canvas.create_line(0, i * 4, 700, i * 4, fill=color)

# Initialize the main window
root = tk.Tk()
root.title("Creative Translator")
root.geometry("700x500")
root.resizable(False, False)

# Create a canvas for gradient background
canvas = Canvas(root, width=700, height=500)
canvas.pack(fill='both', expand=True)
create_gradient(canvas, "#FFB6C1", "#1E90FF")

# Frame for content
content_frame = ttk.Frame(root)
content_frame.place(relx=0.5, rely=0.5, anchor='center')

# Style the widgets
style = ttk.Style(root)
style.configure('TButton', font=('Helvetica', 12, 'bold'), foreground='black', background='#FF6347', padding=10)
style.configure('TLabel', font=('Helvetica', 14, 'bold'), foreground='#00008B')  # Dark blue font color
style.configure('TCombobox', font=('Helvetica', 12))
style.map('TButton', background=[('active', '#FF4500')])

# Create labels and text input/output fields
ttk.Label(content_frame, text="Enter Text:").grid(row=0, column=0, pady=10, sticky='w')
text_input = tk.Text(content_frame, height=6, width=50, font=('Helvetica', 12), bg="#F8F8FF", fg="#000000", bd=0)
text_input.grid(row=1, column=0, pady=5, padx=10, sticky='we')

ttk.Label(content_frame, text="Translated Text:").grid(row=2, column=0, pady=10, sticky='w')
text_output = tk.Text(content_frame, height=6, width=50, font=('Helvetica', 12), bg="#F8F8FF", fg="#000000", bd=0)
text_output.grid(row=3, column=0, pady=5, padx=10, sticky='we')

# Language selection dropdowns
lang_frame = ttk.Frame(content_frame)
lang_frame.grid(row=4, column=0, pady=20)

ttk.Label(lang_frame, text="From:").grid(row=0, column=0, padx=10, sticky='e')
source_lang = ttk.Combobox(lang_frame, values=languages, state='readonly')
source_lang.set("English")
source_lang.grid(row=0, column=1, padx=10)

ttk.Label(lang_frame, text="To:").grid(row=0, column=2, padx=10, sticky='e')
target_lang = ttk.Combobox(lang_frame, values=languages, state='readonly')
target_lang.set("Spanish")
target_lang.grid(row=0, column=3, padx=10)

# Create rounded Translate button
translate_button = ttk.Button(content_frame, text="Translate", command=translate_text, style='TButton')
translate_button.grid(row=5, column=0, pady=10)

# Overlay the canvas with the content frame
canvas.create_window(350, 250, window=content_frame)

# Start the Tkinter event loop
root.mainloop()
