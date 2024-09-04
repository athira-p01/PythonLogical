import tkinter as tk
from tkinter import messagebox

# Function to encrypt the message
def encrypt_message():
    shift = int(shift_entry.get())
    plaintext = text_entry.get("1.0", "end-1c")
    ciphertext = ''.join([chr(((ord(char) - 65 + shift) % 26) + 65) if char.isupper()
                          else chr(((ord(char) - 97 + shift) % 26) + 97) if char.islower()
                          else char for char in plaintext])
    result_text.delete("1.0", "end")
    result_text.insert(tk.END, ciphertext)

# Function to decrypt the message
def decrypt_message():
    shift = int(shift_entry.get())
    ciphertext = text_entry.get("1.0", "end-1c")
    plaintext = ''.join([chr(((ord(char) - 65 - shift) % 26) + 65) if char.isupper()
                          else chr(((ord(char) - 97 - shift) % 26) + 97) if char.islower()
                          else char for char in ciphertext])
    result_text.delete("1.0", "end")
    result_text.insert(tk.END, plaintext)

# Function to validate the shift input
def validate_shift_input(new_value):
    if new_value.isdigit() or new_value == "":
        return True
    else:
        messagebox.showerror("Invalid input", "Please enter a valid integer for the shift.")
        return False

# Create the main window
root = tk.Tk()
root.title("Encrypt/Decrypt Tool")

# Set up the layout with different structure

# Frame for Input and Options
input_frame = tk.Frame(root)
input_frame.pack(pady=10, padx=10, fill="x")

# Message Entry
tk.Label(input_frame, text="Enter your message :").pack(anchor="w")
text_entry = tk.Text(input_frame, height=5, width=50)
text_entry.pack()

# Shift Entry
tk.Label(input_frame, text="Enter the key :").pack(anchor="w")
shift_entry = tk.Entry(input_frame, validate="key", validatecommand=(root.register(validate_shift_input), "%P"))
shift_entry.pack(pady=5)

# Frame for Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

# Encrypt and Decrypt Buttons
tk.Button(button_frame, text="Encrypt", width=15, command=encrypt_message).pack(side="left", padx=5)
tk.Button(button_frame, text="Decrypt", width=15, command=decrypt_message).pack(side="left", padx=5)

# Frame for Result
result_frame = tk.Frame(root)
result_frame.pack(pady=10, padx=10, fill="x")

# Result Display
tk.Label(result_frame, text="Result:").pack(anchor="w")
result_text = tk.Text(result_frame, height=5, width=50)
result_text.pack()

# Start the Tkinter main loop
root.mainloop()
