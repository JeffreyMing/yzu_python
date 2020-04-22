import random as r

t = 0
while True:
    n = r.randint(1, 100)
    t += 1
    if n == 50:
        break
    if n % 3 != 0:
        continue
    print(t, n)
