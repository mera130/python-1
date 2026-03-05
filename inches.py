import tkinter as tk
from tkinter import messagebox

def convert_to_cm():
    try:
        inches = float(entry.get())
        centimeters = inches * 2.54
        result_label.config(text=f"{inches} inches = {centimeters:.2f} cm")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")

root = tk.Tk()
root.title("Inches to Centimeters Converter")
root.geometry("350x200")
root.resizable(False, False)

title_label = tk.Label(root, text="Length Converter", font=("Arial", 14))
title_label.pack(pady=10)

entry_label = tk.Label(root, text="Enter length in inches:")
entry_label.pack()

entry = tk.Entry(root, width=20)
entry.pack(pady=5)

convert_button = tk.Button(root, text="Convert", command=convert_to_cm)
convert_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=5)

root.mainloop()