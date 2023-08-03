import tkinter as tk
from tkinter import Toplevel, Label
from PIL import Image, ImageTk

class OptionImageApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Option Image Viewer")
        
        #option names as key and image as values
        self.options = {
            "Option 1- XXXTENTACION": "miniproj/images/doodletentacion.jpg",
            "Option 2- 21 SAVAGE": "miniproj/images/doodle21.jpg",
            "Option 3- DRAKE": "miniproj/images/doodledrake.jpg",
            "Option 4- EMINEM": "miniproj/images/doodleeminem.jpg",
            "Option 5- KANYE WEST": "miniproj/images/doodlekanye.jpg",
            "Option 6- A$AP ROCKY": "miniproj/images/doodlerocky.jpg",
            "Option 7- TRAVIS SCOTT": "miniproj/images/doodletravis.jpg",
            "Option 8- POST MALONE": "miniproj/images/doodlepost.jpg",
            "Option 9- 2PAC": "miniproj/images/doodle2pac.jpg",
            "Option 10- WEEKND": "miniproj/images/doodleweeknd.jpg",
        }

        self.selected_option = tk.StringVar()

        #button for all options
        for option in self.options:
            tk.Radiobutton(
                root,
                text=option,
                variable=self.selected_option,
                value=option,
                command=self.show_image_messagebox,
            ).pack(anchor="w")

    def show_image_messagebox(self):
        option = self.selected_option.get()
        if option in self.options:
            image_filename = self.options[option]
            image = Image.open(image_filename)

            top = Toplevel(self.root)
            top.title(option)

            photo = ImageTk.PhotoImage(image)
            image_label = Label(top, image=photo)
            image_label.image = photo
            image_label.pack()
        else:
            tk.messagebox.showinfo("Error", "Image not found.")

if __name__ == "__main__":
    root = tk.Tk()
    app = OptionImageApp(root)
    root.mainloop()
