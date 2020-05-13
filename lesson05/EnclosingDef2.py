def add(n):
    def calc(w):
        return n * (1+w)
    return calc

x = add(100)
print("%.2f" % x(0.1))
print("%.2f" % x(0.2))
print("%.2f" % x(0.3))

print("%.2f" % add(200)(0.1))