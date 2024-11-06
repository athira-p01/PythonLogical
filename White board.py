import tkinter as tk
from tkinter.colorchooser import askcolor
from PIL import Image, ImageDraw


class DigitalWhiteBoard:
    def __init__(self, root):
        self.root = root
        self.root.title("Digital Whiteboard")
        self.root.geometry("800x600")

        # Initialize color and brush size
        self.brush_color = "black"
        self.brush_size = 5

        # Create Canvas
        self.canvas = tk.Canvas(self.root, bg="white", width=800, height=500)
        self.canvas.pack(pady=20)

        # Create a PIL Image to save drawings
        self.image = Image.new("RGB", (800, 500), "white")
        self.draw = ImageDraw.Draw(self.image)

        # Bind mouse events to canvas
        self.canvas.bind("<B1-Motion>", self.paint)
        self.canvas.bind("<ButtonRelease-1>", self.reset)

        # Create buttons for controls
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)

        color_button = tk.Button(button_frame, text="Select Color", command=self.select_color)
        color_button.grid(row=0, column=0, padx=5)

        size_button = tk.Button(button_frame, text="Brush Size", command=self.set_brush_size)
        size_button.grid(row=0, column=1, padx=5)

        clear_button = tk.Button(button_frame, text="Clear", command=self.clear_canvas)
        clear_button.grid(row=0, column=2, padx=5)

        save_button = tk.Button(button_frame, text="Save", command=self.save_image)
        save_button.grid(row=0, column=3, padx=5)

        # Variables to track drawing position
        self.old_x = None
        self.old_y = None

    def select_color(self):
        color = askcolor(color=self.brush_color)[1]
        if color:
            self.brush_color = color

    def set_brush_size(self):
        size_window = tk.Toplevel(self.root)
        size_window.title("Brush Size")
        tk.Label(size_window, text="Select Brush Size:").pack(pady=5)
        size_slider = tk.Scale(size_window, from_=1, to=20, orient="horizontal")
        size_slider.set(self.brush_size)
        size_slider.pack(pady=5)

        def apply_size():
            self.brush_size = size_slider.get()
            size_window.destroy()

        tk.Button(size_window, text="Apply", command=apply_size).pack(pady=10)

    def paint(self, event):
        if self.old_x and self.old_y:
            # Draw on the canvas
            self.canvas.create_line(self.old_x, self.old_y, event.x, event.y, width=self.brush_size,
                                    fill=self.brush_color, capstyle=tk.ROUND, smooth=True)
            # Draw on the PIL image
            self.draw.line([self.old_x, self.old_y, event.x, event.y], fill=self.brush_color, width=self.brush_size)

        self.old_x = event.x
        self.old_y = event.y

    def reset(self, event):
        self.old_x = None
        self.old_y = None

    def clear_canvas(self):
        self.canvas.delete("all")
        self.draw.rectangle((0, 0, 800, 500), fill="white")

    def save_image(self):
        filename = "whiteboard_drawing.png"
        self.image.save(filename)
        print(f"Image saved as {filename}")


# Run the application
root = tk.Tk()
whiteboard = DigitalWhiteBoard(root)
root.mainloop()
