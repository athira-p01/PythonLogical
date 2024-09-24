import fitz  # PyMuPDF
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk


class PDFViewer:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Viewer")

        # Open PDF button at the top
        self.open_button = tk.Button(self.root, text="Open PDF", command=self.open_pdf)
        self.open_button.pack(side=tk.TOP, fill=tk.X)

        # Main frame with canvas and scrollbar
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Canvas for displaying PDF pages
        self.canvas = tk.Canvas(self.main_frame)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Scrollbar for vertical scrolling
        self.scrollbar = tk.Scrollbar(self.main_frame, orient=tk.VERTICAL, command=self.on_scroll)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.canvas.config(yscrollcommand=self.scrollbar.set)

        # Bind the mouse wheel to scroll functionality
        self.canvas.bind("<MouseWheel>", self.mouse_scroll)

        # PDF variables
        self.doc = None
        self.page_num = 0
        self.total_pages = 0
        self.page_height = 0

    def open_pdf(self):
        file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
        if not file_path:
            return

        try:
            self.doc = fitz.open(file_path)
            self.page_num = 0
            self.total_pages = self.doc.page_count
            self.show_page(self.page_num)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to open PDF: {str(e)}")

    def show_page(self, page_num):
        if self.doc is None:
            return

        # Load the page and render it as an image
        page = self.doc.load_page(page_num)
        pix = page.get_pixmap()

        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        self.img_tk = ImageTk.PhotoImage(img)

        # Adjust canvas and scrollbar to fit the image size
        self.page_height = pix.height
        self.canvas.config(scrollregion=(0, 0, pix.width, pix.height))

        # Clear the canvas and display the new page
        self.canvas.delete("all")
        self.canvas.create_image(0, 0, image=self.img_tk, anchor=tk.NW)

    def on_scroll(self, *args):
        self.canvas.yview(*args)

        # Change page when scrollbar reaches top or bottom
        if float(self.canvas.yview()[1]) == 1.0 and self.page_num < self.total_pages - 1:
            self.page_num += 1
            self.show_page(self.page_num)
            self.canvas.yview_moveto(0)
        elif float(self.canvas.yview()[0]) == 0.0 and self.page_num > 0:
            self.page_num -= 1
            self.show_page(self.page_num)
            self.canvas.yview_moveto(1)

    def mouse_scroll(self, event):
        # Scroll with the mouse wheel
        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

        # Change page when scrolling to the top or bottom
        if float(self.canvas.yview()[1]) == 1.0 and self.page_num < self.total_pages - 1:
            self.page_num += 1
            self.show_page(self.page_num)
            self.canvas.yview_moveto(0)
        elif float(self.canvas.yview()[0]) == 0.0 and self.page_num > 0:
            self.page_num -= 1
            self.show_page(self.page_num)
            self.canvas.yview_moveto(1)


if __name__ == "__main__":
    root = tk.Tk()
    app = PDFViewer(root)
    root.geometry("800x600")
    root.mainloop()
