import pyvisa
import time
import os
from PIL import Image, ImageTk
def grab(filename='rigol.bmp', seconds=1):
    rigol = pyvisa.ResourceManager().open_resource(pyvisa.ResourceManager().list_resources()[0])
    buf = rigol.query_binary_values(':DISP:DATA?', datatype='B')
    with open(filename, 'wb') as f:
        f.write(bytearray(buf))
    img = Image.open('rigol.bmp')
    img.save( 'rigol.png', 'png')
grab()

from tkinter import *
import PIL.Image
win = Tk()

# Define the geometry of the window
win.geometry("700x500")

frame = Frame(win, width=1024, height=600)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)
# Create an object of tkinter ImageTk
img = ImageTk.PhotoImage(PIL.Image.open("rigol.png"))

# Create a Label Widget to display the text or Image
label = Label(frame, image = img)
label.pack()

#refresh image
def update_image(self):
    # reload the updated result_veg.jpeg
    self.update_img = ImageTk.PhotoImage(file='result_veg.jpeg')
    self.Preview_Image.itemconfig(self.image_id, image=self.update_img)

while True:
    grab()
    win.update()
    win.after(1000, update_image)
    time.sleep(1)
win.mainloop()
