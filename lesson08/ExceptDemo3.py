def input_number():
    x = 10
    try:
        y = int(input('請輸入數字:'))
        z = x / y
    except ZeroDivisionError as e:
        print('分母不可為0', e)
        input_number()
    except ValueError as e:
        print('資料輸入錯誤', e)
        input_number()
    else:
        print(z)

if __name__ == '__main__':
    input_number()