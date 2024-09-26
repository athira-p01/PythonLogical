import tkinter as tk
from tkinter import messagebox

class BillManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Bill Management System")
        self.root.geometry("500x600")
        self.root.config(bg="#f2f2f2")  # Light background for aesthetics

        # Variables
        self.customer_name = tk.StringVar()
        self.customer_contact = tk.StringVar()
        self.items = {"Tea": 10, "Coffee": 15, "Dosa": 30, "Idli": 20, "Cookies": 10, "Juice": 25}
        self.item_quantity = {}

        # Title
        title = tk.Label(self.root, text="Billing System", font=("Helvetica", 24, "bold"), bg="#b0e0e6", fg="black")
        title.pack(fill=tk.BOTH)

        # Customer Details
        self.customer_frame = tk.Frame(self.root, bg="#e6e6fa", bd=3, relief=tk.GROOVE)
        self.customer_frame.place(x=10, y=60, width=480, height=100)

        self.lbl_name = tk.Label(self.customer_frame, text="Customer Name:", bg="#e6e6fa", font=("Arial", 12, "bold"))
        self.lbl_name.grid(row=0, column=0, padx=10, pady=5)
        self.entry_name = tk.Entry(self.customer_frame, textvariable=self.customer_name, font=("Arial", 12))
        self.entry_name.grid(row=0, column=1, padx=10, pady=5)

        self.lbl_contact = tk.Label(self.customer_frame, text="Contact No:", bg="#e6e6fa", font=("Arial", 12, "bold"))
        self.lbl_contact.grid(row=1, column=0, padx=10, pady=5)
        self.entry_contact = tk.Entry(self.customer_frame, textvariable=self.customer_contact, font=("Arial", 12))
        self.entry_contact.grid(row=1, column=1, padx=10, pady=5)

        # Items Section
        self.items_frame = tk.Frame(self.root, bg="#f5f5f5", bd=3, relief=tk.GROOVE)
        self.items_frame.place(x=10, y=170, width=480, height=250)

        self.lbl_items = tk.Label(self.items_frame, text="Select Items", bg="#f5f5f5", font=("Arial", 16, "bold"))
        self.lbl_items.grid(row=0, column=0, padx=10, pady=5)

        self.item_vars = {}
        row = 1
        for item, price in self.items.items():
            self.item_vars[item] = tk.IntVar(value=0)  # Initial quantity as 0
            tk.Label(self.items_frame, text=f"{item} (₹{price})", font=("Arial", 12), bg="#f5f5f5").grid(row=row, column=0, padx=10, pady=5)
            tk.Entry(self.items_frame, textvariable=self.item_vars[item], width=5).grid(row=row, column=1, padx=10, pady=5)
            row += 1

        # Bill Area
        self.bill_frame = tk.Frame(self.root, bg="#d3d3d3", bd=3, relief=tk.GROOVE)
        self.bill_frame.place(x=10, y=430, width=480, height=150)

        self.txtarea = tk.Text(self.bill_frame, font=("Arial", 12), bg="#ffffff")
        self.txtarea.pack(fill=tk.BOTH)

        # Buttons
        self.btn_frame = tk.Frame(self.root, bg="#dcdcdc")
        self.btn_frame.place(x=10, y=580, width=480, height=40)

        self.btn_generate = tk.Button(self.btn_frame, text="Generate Bill", font=("Arial", 12, "bold"), command=self.generate_bill)
        self.btn_generate.pack(side=tk.LEFT, padx=10, pady=5)

        self.btn_total = tk.Button(self.btn_frame, text="Calculate Total", font=("Arial", 12, "bold"), command=self.calculate_total)
        self.btn_total.pack(side=tk.LEFT, padx=10, pady=5)

        self.btn_clear = tk.Button(self.btn_frame, text="Clear", font=("Arial", 12, "bold"), command=self.clear)
        self.btn_clear.pack(side=tk.RIGHT, padx=10, pady=5)

        self.total_price = tk.DoubleVar()

    def calculate_total(self):
        total = 0
        for item, price in self.items.items():
            quantity = self.item_vars[item].get()
            total += price * quantity
        self.total_price.set(total)
        messagebox.showinfo("Total", f"Total Bill: ₹{total}")

    def generate_bill(self):
        # Customer details
        name = self.customer_name.get()
        contact = self.customer_contact.get()

        if not name or not contact:
            messagebox.showerror("Error", "Customer details are required!")
            return

        # Start the bill
        self.txtarea.delete('1.0', tk.END)
        self.txtarea.insert(tk.END, f"Customer Name: {name}\n")
        self.txtarea.insert(tk.END, f"Contact No: {contact}\n")
        self.txtarea.insert(tk.END, "-" * 50 + "\n")
        self.txtarea.insert(tk.END, "Items\t\tQty\t\tPrice\n")
        self.txtarea.insert(tk.END, "-" * 50 + "\n")

        total_price = 0
        for item, price in self.items.items():
            quantity = self.item_vars[item].get()
            if quantity > 0:
                self.txtarea.insert(tk.END, f"{item}\t\t{quantity}\t\t₹{price * quantity}\n")
                total_price += price * quantity

        self.txtarea.insert(tk.END, "-" * 50 + "\n")
        self.txtarea.insert(tk.END, f"Total Bill:\t\t\t₹{total_price}\n")
        self.txtarea.insert(tk.END, "-" * 50 + "\n")

    def clear(self):
        self.customer_name.set("")
        self.customer_contact.set("")
        for var in self.item_vars.values():
            var.set(0)
        self.txtarea.delete('1.0', tk.END)
        self.total_price.set(0)


# Running the app
root = tk.Tk()
app = BillManagementSystem(root)
root.mainloop()
