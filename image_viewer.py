import os
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

from image_loader import list_files_by_extension

class ImageLabeler:
    def __init__(self, root, file_list):
        self.root = root
        self.file_list = file_list
        self.current_index = 0
        self.labels = {}

        self.image_label = ttk.Label(root)
        self.image_label.pack(expand=True)

        self.label_entry = ttk.Entry(root)
        self.label_entry.pack()
        self.label_entry.bind("<Return>", self.save_label)

        self.root.bind("<Up>", self.show_previous_image)
        self.root.bind("<Down>", self.show_next_image)

        self.display_image()

    def save_label(self, event):
        label = self.label_entry.get()
        if label.isdigit():
            self.labels[self.file_list[self.current_index]] = int(label)
            self.label_entry.delete(0, tk.END)
            self.show_next_image()
        else:
            print("Please enter a valid number.")

    def display_image(self):
        image_path = self.file_list[self.current_index]
        image = Image.open(image_path)
        image.thumbnail((800, 600))
        photo = ImageTk.PhotoImage(image)
        self.image_label.config(image=photo)
        self.image_label.image = photo

    def show_next_image(self, event=None):
        if self.current_index < len(self.file_list) - 1:
            self.current_index += 1
            self.display_image()

    def show_previous_image(self, event=None):
        if self.current_index > 0:
            self.current_index -= 1
            self.display_image()

if __name__ == "__main__":
    file_list = list_files_by_extension("/media/aoi/3d665531-14ca-489a-b213-db08402e7cab/dataset/bridge/ngs_lianxis")

    root = tk.Tk()
    root.title("Image Labeler")

    labeler = ImageLabeler(root, file_list)

    root.mainloop()
