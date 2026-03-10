from tkinter import *
from tkinter import messagebox
from PIL import Image , ImageTk
root = Tk()
root.title('denomination calculator')
root.configure('bg = light blue')
root.geometry('650x400')

upload = Image.open('black.webp')
upload = upload.resize((300,300))
image = ImageTk.photoImage(upload)
label = Label(root, image=image, bg='light blue')
label.place(x= 180, y=120)
label1 = Label(
    root, 
    text = 'hey! welcome to denomination calculator',
    bg = 'light blue'
)
label1.place(relx= 0.5, y = 340, anchor=CENTER)

def msg():
    msg_box = messagebox.showinfo(
        'alert',
        'do you want to calculate the denomination count?', 
    )
    if msg== 'ok':
        topwin()
        
button1 = Button(
    root, 
    text="let's get started",
    command=msg,
    bg = 'brown', 
    fg = 'white'
)

button1.place(x=260, y= 360)
def topwin():
    top = Toplevel()
    top.title('denomination calculator')
    top.configure(bg = 'light grey')
    top.geometry('600x350+50+50')
    label = Label(top, text = 'enter the total amount: ', bg = 'light grey')
    
    