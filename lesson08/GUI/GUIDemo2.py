import tkinter

win = tkinter.Tk()
win.title('我的小視窗')
win.geometry('300x300')

label1 = tkinter.Label(win, text = 'Hello')
label2 = tkinter.Label(win, text = 'Hello2')
button1 = tkinter.Button(win, text = 'Hello3')
label4 = tkinter.Label(win, text = 'Hello4')
button2 = tkinter.Button(win, text = 'Hello5')
label1.grid(column=0, row=0)
label2.grid(column=1, row=0)
button1.grid(column=1, row=1)
label4.grid(column=2, row=1)
button2.grid(column=3, row=2)

win.mainloop()