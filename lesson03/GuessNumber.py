import random as r
ans = r.randint(1, 99)

min = 0
max = 100

count = 0
while True:
    count += 1
    guess = int(input("(第%d次)請輸入數字 %d ~ %d :" % (count, min, max)))
    if count == 7:
        print("GG了")
        break
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