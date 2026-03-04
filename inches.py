import tkinter as tk
from tkinter import messagebox
    try:
       inches = float(entry.get())
       cm = inches*2.4
       result_label.config(text = f'{inches} inches= {cm:.2f}cm')
    except ValueError:
        messagebox.showwarning('invalid input', 'please enter a valid NUMBER')
root = tk.Tk()
root.title('inches to cm')
root.geometry('350x200')
root.resizable(False, False)
title_label = tk.Label(root, text='length converter', font=('ariel', 14))
title_label.pack(pady=40)

event_label = tk.Label(root, text='enter the length (in inches)')
event_label.pack()

