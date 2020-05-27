import tkinter

win = tkinter.Tk()
win.title('我的小視窗')
win.geometry('300x300')

label1 = tkinter.Label(win, text = 'Hello')
label1.pack(side = tkinter.LEFT)
label2 = tkinter.Label(win, text = 'Hello2')
label2.pack(side = tkinter.RIGHT)

win.mainloop()