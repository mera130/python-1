import tkinter as tk
from tkinter import messagebox , ttk
class restaurantMangement():
    def __init__(self, root):
        self.root = root
        self.root.title('restaurant mangement ')
        
        self.menu_items = {
            'french fries' : 2,
            'lunch ' : 2,
            'chesese burger' : 2.5,
            'drinks' : 1, 
            'pizza' : 4
            
        }
        self_exchange = 122
        self.setup_background(root)
        
        frame = ttk.Frame(root)
        frame.place(relx = 0.5, rely = 0.5, anchor= tk.CENTER)
        ttk.Label(
            frame, 
            text='restaurent mangement'
            font=('Ariel', 20, 'bold')
        ).grid(row = 0, columnspan = 3, padx = 10, pady = 10)
        
        self.menu_label = {}
        self.menu_quantities = {}
        
        for i, ( items, price) in enumerate(self.menu_items.items(), start = 1 ):
            label = ttk.Label(
                frame , 
                text = f"{items} (${price}): "
                font = ('Ariel', 12)
            )
            label.grid(row = i, column = 0, padx = 10, pady = 5)
            self.menu_label[items] = label
            
            quantity_entry = ttk.Entry(frame, width = 5)
            quantity_entry.grid(row = i , column = 1, padx = 10, pady = 5)
            self.menu_quantities[items]= quantity_entry
        self.currency_var = tk.StringVar()
        ttk.Label(
            frame,
            text='currency'
            font =('Ariel', 12)
        ).grid(
            row = len(self.menu_items) + 1,
            column = 0, 
            padx = 10
            pady = 5,
        )
        
        currency_dropdown = ttk.Combobox(
            frame,
            textvariable=self.currency_var,
            state = 'raedonly',
            width = 18,
            values = ('USD', 'BDT')
            
        )
        currency_dropdown.grid(
            row = len(self.menu_items) + 1,
            column = 0, 
            padx = 10
            pady = 5,
        )
        
        
        
        
    
    
