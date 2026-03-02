from tkinter import *
root = Tk()
root.title('login')
root.geometry('400x400')
frame = Frame(master = root, height=200, width=300, bg='#FBF6F6')
lab1 = Label(frame, text = 'full name', bg='#D96868', fg = 'white', width=12)
lab2 = Label(frame, text = 'email', bg='#D96868', fg = 'white', width=12)
lab3 = Label(frame, text = 'password', bg='#D96868', fg = 'white', width=12)

name_entry = Entry(frame)
email_entry = Entry(frame)
password_entry = Entry(frame, show = '*')

def display():
    name = name_entry.get()
    greet = 'hey'+ name + '!'
    message = '\n congratulation on your new account!!'
    textbox.insert(END, greet)
    textbox.insert(END, message)
    
textbox = Text(bg='#BEBEBE', fg = 'white')
btn = Button(text = 'create account', command=display, bg = "#673030")
frame.place(x = 20, y =0)
lab1.place(x=20, y =20)
name_entry.place(x=150, y= 20)
lab2.place(x= 20, y= 80)
email_entry.place(x= 150, y= 80)
lab3.place(x= 20, y = 140)
password_entry.place(x= 150, y=140)
btn.place(x=130, y= 210)
textbox.place(y= 250)
root.mainloop()

