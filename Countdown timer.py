import tkinter as tk
from tkinter import messagebox
import time

def start_timer():
    try:
        hours = int(hour_entry.get())
        minutes = int(minute_entry.get())
        seconds = int(second_entry.get())
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers.")
        return

    total_seconds = hours * 3600 + minutes * 60 + seconds

    while total_seconds > 0:
        hrs, rem = divmod(total_seconds, 3600)
        mins, secs = divmod(rem, 60)
        timer_display = f'{hrs:02d}:{mins:02d}:{secs:02d}'
        label.config(text=timer_display)
        root.update()
        time.sleep(1)
        total_seconds -= 1

    messagebox.showinfo("Time's up", "Countdown finished!")

# Create the main window
root = tk.Tk()
root.title("Countdown Timer")

# Input for hours, minutes, and seconds
hour_entry = tk.Entry(root, width=10, font=("Helvetica", 16))
hour_entry.grid(row=0, column=0, padx=5, pady=5)
hour_entry.insert(0, "Hours")

minute_entry = tk.Entry(root, width=10, font=("Helvetica", 16))
minute_entry.grid(row=0, column=1, padx=5, pady=5)
minute_entry.insert(0, "Minutes")

second_entry = tk.Entry(root, width=10, font=("Helvetica", 16))
second_entry.grid(row=0, column=2, padx=5, pady=5)
second_entry.insert(0, "Seconds")

# Button to start the countdown
start_button = tk.Button(root, text="Start Timer", command=start_timer, font=("Helvetica", 16))
start_button.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

# Label to display the countdown
label = tk.Label(root, font=("Helvetica", 48))
label.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

# Run the Tkinter event loop
root.mainloop()
