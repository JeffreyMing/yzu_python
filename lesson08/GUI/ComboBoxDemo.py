import tkinter
from tkinter import ttk

win = tkinter.Tk()
win.geometry('300x300')

#fruits = ['apple', 'banana', 'mango', 'watermelon']
fruits ={'apple':50, 'banana':60, 'mango':70, 'watermelon':20}

combo = ttk.Combobox(win, values = list(fruits.keys()), state = 'readonly') # 'readonly' 只能選，'disabled' 完全不給選
combo.current(0)
combo.pack()

win.mainloop()