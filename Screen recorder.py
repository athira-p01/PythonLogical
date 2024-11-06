from tkinter import *
import pyscreenrec

root = Tk()
root.geometry("400x600")
root.title("Screen Recorder")
root.config(bg="#fff")
root.resizable(False,False)

def start_rec():
    file = Filename.get()
    rec.start_recording(str(file+".mp4"), 5)

def pause_rec():
    rec.pause_recording()
def resume_rec():
    rec.resume_recording()
def stop_rec():
    rec.stop_recording()

rec = pyscreenrec.ScreenRecorder()

lbl = Label(root, text="Screen Recorder", bg="#fff", font="ariel 15 bold")
lbl.pack(pady=20)

image1 = PhotoImage(file="recording.png")
Label(root, image=image1, bd=0).pack(pady=30)

Filename = StringVar()
entry = Entry(root, textvariable=Filename, width=15, font="arial 15")
entry.place(x=100, y=350)
Filename.set("recording25")

start = Button(root, text="Start", font="ariel 20", bd=0, command=start_rec)
start.place(x=140, y=250)

image2 = PhotoImage(file="pause.png")
pause = Button(root, image=image2, bd=0, bg="#fff", command=pause_rec)
pause.place(x=50, y=450)

image3 = PhotoImage(file="resume.png")
resume = Button(root, image=image3, bd=0, bg="#fff", command=resume_rec)
resume.place(x=150, y=450)

image4 = PhotoImage(file="stop.png")
stop = Button(root, image=image4, bd=0, bg="#fff", command=stop_rec)
stop.place(x=250, y=450)

root.mainloop()
