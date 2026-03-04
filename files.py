from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
window = Tk()
window.title('files')
window.geometry('600x600')
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)
def open_files():
    filepath = askopenfilename(
        filetypes= [('text files', '*.txt'), ('all files', '*.*')]
        
    )
    if not filepath:
        return
    txt_edit.delete(1.0, END)
    with open(filepath, 'r') as input_file:
        text = input_file.read()
        txt_edit.insert(END, text)
        input_file.close()
    window.title(f'file - {filepath}')
def save_files():
    filepath = asksaveasfilename(
        defaultextension='txt', 
        filetypes= [('text files', '*.txt'), ('all files', '*.*')]
    )
    if not filepath:
        return
    with open(filepath,'w' ) as output_file:
        text = txt_edit.get(1.0, END)
        output_file.write(text)
    window.title(f'file - {filepath}')

txt_edit = Text(window)
fr_button = Frame(window, relief= RAISED, bd = 2)
btn_open = Button(fr_button, text='open', command=open_files )
btn_saves = Button(fr_button, text='save as...', command = save_files)

btn_open.grid(row = 0, column = 0,  sticky= 'ew' ,padx = 5, pady = 5)
btn_saves.grid(row = 1, column = 0,  sticky= 'ew' ,padx = 5)
fr_button.grid(row = 0,column = 0, sticky='ns')
txt_edit.grid(row = 0, column = 1, sticky='nsew')
window.mainloop()

    

