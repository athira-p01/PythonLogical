import tkinter as tk

def click(event):
    text = event.widget.cget("text")
    if text == " ":
        try:
            result = str(eval(screen.get()))
            screen_var.set(result)
        except Exception as e:
            screen_var.set("Error")
    elif text == "C":
        screen_var.set("")
    else:
        screen_var.set(screen_var.get() + text)

root = tk.Tk()
root.title("Calculator")

screen_var = tk.StringVar()
screen = tk.Entry(root, textvar=screen_var, font="lucida 20 bold", bd=10, relief=tk.SUNKEN)
screen.pack(fill=tk.BOTH, ipadx=8)

buttons_frame = tk.Frame(root)
buttons_frame.pack()

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "C", "+"
]

i = 0
for button in buttons:
    btn = tk.Button(buttons_frame, text=button, font="lucida 15 bold", relief=tk.RAISED, bd=5)
    btn.grid(row=i//4, column=i%4, padx=5, pady=5)
    btn.bind("<Button-1>", click)
    i += 1

equal_btn = tk.Button(buttons_frame, text="=", font="lucida 15 bold", relief=tk.RAISED, bd=5)
equal_btn.grid(row=i//4, column=i%4, padx=5, pady=5)
equal_btn.bind("<Button-1>", click)

root.mainloop()
