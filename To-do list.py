import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x400")
root.config(bg="#f5f5f5")
# Function to add a new task
def add_task():
    task = task_entry.get()
    if task != "":
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

# Function to delete the selected task
def delete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

# Function to clear all tasks
def clear_tasks():
    task_listbox.delete(0, tk.END)
# Label
title_label = tk.Label(root, text="To - Do List", font=("Arial Black", 16, "bold"), bg="#f5f5f5", fg="#333")
title_label.pack(pady=10)

# Entry widget for new task input
task_entry = tk.Entry(root, width=40, font=("Helvetica", 12), borderwidth=2)
task_entry.pack(pady=10)

# Buttons for adding, deleting, and clearing tasks
add_button = tk.Button(root, text="Add Task", command=add_task, width=15, font=("Helvetica", 12), bg="#4CAF50", fg="white")
add_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", command=delete_task, width=15, font=("Helvetica", 12), bg="#f44336", fg="white")
delete_button.pack(pady=5)

clear_button = tk.Button(root, text="Clear All Tasks", command=clear_tasks, width=15, font=("Helvetica", 12), bg="#555555", fg="white")
clear_button.pack(pady=5)

# Listbox to display tasks
task_listbox = tk.Listbox(root, width=40, height=15, font=("Helvetica", 12), selectmode=tk.SINGLE, borderwidth=2)
task_listbox.pack(pady=10)

root.mainloop()
