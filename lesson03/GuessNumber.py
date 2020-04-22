import random as r
ans = r.randint(1, 99)

min = 0
max = 100

while True:
    guess = int(input("請輸入數字 %d ~ %d :" % (min, max)))
    # 防呆
    if guess >= max or guess <= min:
        print('超過範圍,請重新輸入')
        continue

    if guess == ans:
        print("恭喜答對了")
        break
    elif guess < ans:
        min = guess
    else:
        max = guess