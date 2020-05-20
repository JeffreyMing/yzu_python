class Father:
    money = 0
    def __init__(self, money):
        self.money = money
    def __str__(self):
        return "money = " + str(self.money)

class Son(Father): # 繼承father
    age = 0
    def __init__(self, money, age):
        Father.__init__(self, money) # 在子類別初始化後可繼承父類別的money
        self.age = age
    def __str__(self):
        return Father.__str__(self) + " son age = " + str(Son.age)  #呼叫father的__str__

if __name__ == '__main__':
    son = Son(50000, 10)
    print(son.age, son.money)
    print(son)
