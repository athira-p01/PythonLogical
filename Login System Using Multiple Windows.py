import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
import time

# Sample login credentials
USERNAME = "admin"
PASSWORD = "password123"

# Stopwatch functionality
running = False
counter = 0


def update_time():
    if running:
        global counter
        counter += 1
        time_display.config(text=convert_time(counter))
        stopwatch_window.after(1000, update_time)  # Update every 1 second


def convert_time(seconds):
    mins, secs = divmod(seconds, 60)
    hrs, mins = divmod(mins, 60)
    return f"{hrs:02}:{mins:02}:{secs:02}"


def start_stopwatch():
    global running
    if not running:
        running = True
        update_time()


def stop_stopwatch():
    global running
    running = False


def reset_stopwatch():
    global running, counter
    running = False
    counter = 0
    time_display.config(text="00:00:00")


# Function to handle login
def login():
    user = entry_username.get()
    pwd = entry_password.get()

    if user == USERNAME and pwd == PASSWORD:
        messagebox.showinfo("Login Success", "Welcome!")
        login_window.destroy()  # Close login window
        open_stopwatch()  # Open stopwatch window
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")


# Function to open the stopwatch window
def open_stopwatch():
    global stopwatch_window, time_display

    # Create stopwatch window
    stopwatch_window = tk.Tk()
    stopwatch_window.title("Stopwatch")
    stopwatch_window.geometry("400x500")


    # Stylish display for stopwatch time
    time_display = tk.Label(stopwatch_window, text="00:00:00", font=("Helvetica", 40, "bold"),
                            bg="#e6e6fa", fg="#2f4f4f", borderwidth=2, relief="solid")
    time_display.pack(pady=50)

    # Start button with image
    try:
        start_img = PhotoImage(file="start_button.png")  # Replace with your start button image path
        btn_start = tk.Button(stopwatch_window, image=start_img, command=start_stopwatch,
                              bg="#ffffff", border=0)
        btn_start.pack(side=tk.LEFT, padx=20, pady=20)
    except Exception as e:
        btn_start = tk.Button(stopwatch_window, text="Start", font=("Helvetica", 12, "bold"), command=start_stopwatch,
                              bg="#4caf50", fg="#ffffff", padx=10, pady=5)
        btn_start.pack(side=tk.LEFT, padx=20, pady=20)

    # Stop button with image
    try:
        stop_img = PhotoImage(file="stop_button.png")  # Replace with your stop button image path
        btn_stop = tk.Button(stopwatch_window, image=stop_img, command=stop_stopwatch,
                             bg="#ffffff", border=0)
        btn_stop.pack(side=tk.LEFT, padx=20, pady=20)
    except Exception as e:
        btn_stop = tk.Button(stopwatch_window, text="Stop", font=("Helvetica", 12, "bold"), command=stop_stopwatch,
                             bg="#f44336", fg="#ffffff", padx=10, pady=5)
        btn_stop.pack(side=tk.LEFT, padx=20, pady=20)

    # Reset button with image
    try:
        reset_img = PhotoImage(file="reset_button.png")  # Replace with your reset button image path
        btn_reset = tk.Button(stopwatch_window, image=reset_img, command=reset_stopwatch,
                              bg="#ffffff", border=0)
        btn_reset.pack(side=tk.LEFT, padx=20, pady=20)
    except Exception as e:
        btn_reset = tk.Button(stopwatch_window, text="Reset", font=("Helvetica", 12, "bold"), command=reset_stopwatch,
                              bg="#ff9800", fg="#ffffff", padx=10, pady=5)
        btn_reset.pack(side=tk.LEFT, padx=20, pady=20)

    # Exit button
    btn_exit = tk.Button(stopwatch_window, text="Exit", font=("Helvetica", 12), command=stopwatch_window.destroy,
                         bg="#ff6f61", fg="#ffffff", padx=10, pady=5)
    btn_exit.pack(pady=20)

    stopwatch_window.mainloop()


# Main login window
login_window = tk.Tk()
login_window.title("Login")
login_window.geometry("400x300")
login_window.configure(bg="#f0f0f5")

# Username label and entry
label_username = tk.Label(login_window, text="Username:", font=("Helvetica", 12, "bold"), bg="#f0f0f5", fg="#2f4f4f")
label_username.grid(row=0, column=0, padx=20, pady=20)
entry_username = tk.Entry(login_window, font=("Helvetica", 12))
entry_username.grid(row=0, column=1, padx=20, pady=20)

# Password label and entry
label_password = tk.Label(login_window, text="Password:", font=("Helvetica", 12, "bold"), bg="#f0f0f5", fg="#2f4f4f")
label_password.grid(row=1, column=0, padx=20, pady=20)
entry_password = tk.Entry(login_window, show="*", font=("Helvetica", 12))
entry_password.grid(row=1, column=1, padx=20, pady=20)

# Login button
btn_login = tk.Button(login_window, text="Login", font=("Helvetica", 12, "bold"), command=login,
                      bg="#4169e1", fg="#ffffff", padx=20, pady=5)
btn_login.grid(row=2, column=1, pady=20)

login_window.mainloop()
