import cv2
from tkinter import Tk, Button, Label, filedialog
from PIL import Image, ImageTk

def open_image():
    
    filepath = filedialog.askopenfilename()
    if filepath:
       
        image = cv2.imread(filepath)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) 
        image = Image.fromarray(image) 
        image = ImageTk.PhotoImage(image) 
        
        image_label.config(image=image)
        image_label.image = image  


root = Tk()
root.title("Image Viewer")


Button(root, text="Open Image", command=open_image).pack()


image_label = Label(root)
image_label.pack()

root.mainloop()
