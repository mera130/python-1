from tkinter import *
from datetime import datetime

root = Tk()
root.title('Age Calculator')
root.geometry('400x400')
frame = Frame(master=root, height=200, width=360, bg="#ECE7D1")

lbl1 = Label(frame, text="Full Name", bg="#8E977D", fg="white", width=12)
lbl2 = Label(frame, text="Birth Year", bg="#8E977D", fg="white", width=12)

name_entry = Entry(frame)
birth_entry = Entry(frame)
def calculate_age():
    name = name_entry.get()
    birth_year = int(birth_entry.get())

    current_year = datetime.now().year
    age = current_year - birth_year

    textbox.insert(END, "Hello " + name + "! \n")
    textbox.insert(END, "Your age is: " + str(age) + " years\n")

textbox = Text(bg="#A2CB8B", fg="black")
btn = Button(text="Calculate Age", command=calculate_age, bg="#837C64")

frame.place(x=20, y=0)
lbl1.place(x=20, y=20)
name_entry.place(x=150, y=20)

lbl2.place(x=20, y=80)
birth_entry.place(x=150, y=80)

btn.place(x=130, y=150)
textbox.place(y=220)
root.mainloop()