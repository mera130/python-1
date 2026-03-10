from tkinter import *
root = Tk()
root.geometry('400x300')
root.title('main window')

def topwin():
    top = Toplevel()
    top.geometry('180x200')
    top.title('top window')
    l2 = Label(top, text='this is a toplevel window')
    l2.pack()
    top.mainloop()
l = Label(root , text='this is the main window')
btn = Button(root, text='click here to open another window', command = topwin)
l.pack()
btn.pack()
root.mainloop()