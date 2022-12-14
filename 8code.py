import tkinter
from tkinter import *
root = Tk()
root.title('Button')
root.configure(bg='red')

Button(text='Button', bg='red').pack(side=BOTTOM)
root.mainloop()