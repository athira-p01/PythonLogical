import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# Function to calculate age
def calculate_age():
    try:
        birth_date = datetime(int(entry_year.get()), int(entry_month.get()), int(entry_day.get()))
        today = datetime.today()
        age_years = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        age_months = (today.month - birth_date.month) % 12
        age_days = (today.day - birth_date.day) % 30  # Simplified day difference
        messagebox.showinfo("Your Age", f"{entry_name.get()}, you are {age_years} years, {age_months} months, and {age_days} days old!")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers for Year, Month, and Day.")

# Creating the main window
root = tk.Tk()
root.title("Age Calculator")
root.geometry("400x300")
root.config(bg="#f0f8ff")

# Labels and entry fields
label_heading = tk.Label(root, text="AGE CALCULATOR", font=("Times New Roman", 15, "bold"), fg="white", bg="#4682b4", relief="raised", bd=5)
label_heading.pack(pady=10)

# Name entry
frame_name = tk.Frame(root, bg="#f0f8ff")
frame_name.pack(pady=5)
label_name = tk.Label(frame_name, text="Name:", font=("Arial", 12), bg="#f0f8ff")
label_name.grid(row=0, column=0, padx=5, pady=5)
entry_name = tk.Entry(frame_name, width=20, font=("Arial", 12))
entry_name.grid(row=0, column=1, padx=5, pady=5)

# Year, Month, Day Entry
frame_date = tk.Frame(root, bg="#f0f8ff")
frame_date.pack(pady=10)

label_year = tk.Label(frame_date, text="Year:", font=("Arial", 12), bg="#f0f8ff")
label_year.grid(row=0, column=0, padx=5, pady=5)
entry_year = tk.Entry(frame_date, width=5, font=("Arial", 12))
entry_year.grid(row=0, column=1, padx=5, pady=5)

label_month = tk.Label(frame_date, text="Month:", font=("Arial", 12), bg="#f0f8ff")
label_month.grid(row=0, column=2, padx=5, pady=5)
entry_month = tk.Entry(frame_date, width=5, font=("Arial", 12))
entry_month.grid(row=0, column=3, padx=5, pady=5)

label_day = tk.Label(frame_date, text="Day:", font=("Arial", 12), bg="#f0f8ff")
label_day.grid(row=0, column=4, padx=5, pady=5)
entry_day = tk.Entry(frame_date, width=5, font=("Arial", 12))
entry_day.grid(row=0, column=5, padx=5, pady=5)

# 3D Effect Button
btn_calculate = tk.Button(root, text="Calculate Age", font=("Arial", 8, "bold"), bg="#32cd32", fg="white", relief="raised", bd=4, command=calculate_age)
btn_calculate.pack(pady=20)

# Run the main event loop
root.mainloop()
