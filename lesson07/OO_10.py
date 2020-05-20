# 封裝
class YoyoCard:
    __balance = 0

    @property # 讓balance變成屬性的調用
    def balance(self):
        return self.__balance

    @balance.setter # 讓使用者使用上更直覺
    def balance(self, money):
        self.__balance = self.__balance + money

card = YoyoCard()
print(card.balance)
card.balance = 100
print(card.balance)