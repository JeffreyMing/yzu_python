class Salary:
    def __init__(self, name, money):
        self.name = name
        self.money = money
    def __str__(self): # 提供print出資料
        return self.name + "," + str(self.money)
    def __add__(self, n): # 提供加法使用
        self.money = self.money + n

if __name__ == '__main__':
    s1 = Salary('Mary', 40000)
    s2 = Salary('John', 30000)
    print(s1, s2)
    s1 + 5000
    s2 + 6000
    print(s1, s2)
