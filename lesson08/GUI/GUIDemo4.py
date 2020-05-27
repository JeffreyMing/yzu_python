import tkinter

value = 0

def myadd():
    global value
    value += 1
    var.set(str(value))

win = tkinter.Tk()
win.geometry('300x300')

var = tkinter.StringVar() # 字串變數參照物件

label = tkinter.Label(win, textvariable = var)
label.pack()

button = tkinter.Button(win, text = 'Add', command = myadd)
button.pack()

win.mainloop()