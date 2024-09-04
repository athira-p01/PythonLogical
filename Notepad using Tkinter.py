from tkinter import *
from tkinter import filedialog

root = Tk()
root.geometry("600x600")
root.title("Notepad")
root.config(bg="lightblue")
root.resizable(False, False)

def save_file():
    file_to_save = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    if file_to_save is None:
        return
    text = str(entry.get(1.0, END))
    file_to_save.write(text)
    file_to_save.close()

def open_file():
    file_to_open = filedialog.askopenfile(mode='r', filetypes=[('Text Files', '*.txt')])
    if file_to_open is not None:
        content = file_to_open.read()
        entry.insert(INSERT, content)

b1 = Button(root, width='20', height='2', bg='#fff', text='Save File', command=save_file).place(x=100, y=5)
b2 = Button(root, width='20', height='2', bg='#fff', text='Open File', command=open_file).place(x=300, y=5)

entry = Text(root, height='33', width='72', wrap=WORD)
entry.place(x=10, y=60)

root.mainloop()
