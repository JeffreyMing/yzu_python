def add(n):
    def calc(w):
        return n * (1+w)
    return calc

x = add(100)
print("%.2f" % x(0.3))