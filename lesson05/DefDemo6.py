#攝氏轉華氏
def ctof(c):
    return c*(9/5)+32
print(ctof(35))

#華氏轉氏
def ftoc(f):
    return (f-32)*5/9
print(ftoc(95))

#高階函數
def add(x):
    return x + 1

def sub(x):
    return x - 1

def operate(func, x):
    return func(x)

x = 10
x = operate(add, x)
print(x)
x = operate(sub, x)
print(x)
