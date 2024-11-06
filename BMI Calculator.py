import tkinter as tk
from tkinter import messagebox


# Function to calculate BMI and display health advice
def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get()) / 100  # Convert cm to meters
        age = int(age_entry.get())
        gender = gender_var.get()

        # Calculate BMI
        bmi = weight / (height ** 2)
        bmi = round(bmi, 2)

        # Determine BMI Category
        if bmi < 18.5:
            result = f"Your BMI is {bmi}. You are underweight."
            advice = "Consider gaining weight through a balanced diet rich in proteins and carbohydrates."
        elif 18.5 <= bmi < 24.9:
            result = f"Your BMI is {bmi}. You have a normal weight."
            advice = "Maintain a balanced diet and regular exercise to keep a healthy weight."
        elif 25 <= bmi < 29.9:
            result = f"Your BMI is {bmi}. You are overweight."
            advice = "A combination of a healthy diet and regular exercise can help reduce weight."
        else:
            result = f"Your BMI is {bmi}. You are obese."
            advice = "Consult with a healthcare provider for personalized weight-loss strategies."

        # Display the results and advice
        bmi_result_label.config(text=result, fg="brown")
        health_advice_label.config(text=advice, fg="green")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for weight, height, and age.")


# GUI Setup
window = tk.Tk()
window.title("Advanced BMI Calculator")
window.geometry("450x400")
window.config(bg="lightcyan")

# Title
title_label = tk.Label(window, text="BMI Calculator", font=("Arial", 16, "bold"), bg="lightcyan")
title_label.pack(pady=10)

# Weight Input
weight_label = tk.Label(window, text="Enter your weight (kg):", font=("Arial", 12), bg="lightcyan")
weight_label.pack(pady=5)
weight_entry = tk.Entry(window, font=("Arial", 12))
weight_entry.pack()

# Height Input
height_label = tk.Label(window, text="Enter your height (cm):", font=("Arial", 12), bg="lightcyan")
height_label.pack(pady=5)
height_entry = tk.Entry(window, font=("Arial", 12))
height_entry.pack()

# Age Input
age_label = tk.Label(window, text="Enter your age:", font=("Arial", 12), bg="lightcyan")
age_label.pack(pady=5)
age_entry = tk.Entry(window, font=("Arial", 12))
age_entry.pack()

# Gender Input
gender_label = tk.Label(window, text="Select your gender:", font=("Arial", 12), bg="lightcyan")
gender_label.pack(pady=5)

gender_var = tk.StringVar(value="Select")
gender_frame = tk.Frame(window, bg="lightcyan")
gender_frame.pack()
male_radio = tk.Radiobutton(gender_frame, text="Male", variable=gender_var, value="Male", font=("Arial", 10),
                            bg="lightcyan")
female_radio = tk.Radiobutton(gender_frame, text="Female", variable=gender_var, value="Female", font=("Arial", 10),
                              bg="lightcyan")
male_radio.grid(row=0, column=0, padx=5)
female_radio.grid(row=0, column=1, padx=5)

# Calculate Button
calculate_button = tk.Button(window, text="Calculate BMI", font=("Arial", 12), command=calculate_bmi, bg="lightblue")
calculate_button.pack(pady=10)

# Result Labels
bmi_result_label = tk.Label(window, text="", font=("Arial", 12, "bold"), bg="lightcyan")
bmi_result_label.pack(pady=10)

health_advice_label = tk.Label(window, text="", font=("Arial", 11), bg="lightcyan", wraplength=400)
health_advice_label.pack(pady=10)

window.mainloop()
