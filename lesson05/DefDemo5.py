x = 0  # Global var
y = 0  # Global var
def changeX(n):
    x = n # local var

def changeY(n):
    global y
    y = n # local var

print('x=', x)
changeX(100)
print('x=', x)

print('y=', y)
changeY(100)
print('y=', y)


z = [0]
def changeZ(m, n):
    m[0] = n

print('z=', z)
changeZ(z, 100)
print('z=', z)