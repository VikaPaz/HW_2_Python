max_n = 10000000000
min_n = 0
count1 = 1
count2 = 1

while True:
    num = int(input())
    if num > max_n:
        count1 += 1
    else:
        count1 = 1
    max_n = num
    if num < min_n:
        count2 += 1
    else:
        count2 = 1
    min_n = num

    if num == 0:
        break

if count1 > count2:
    print(count1)
else:
    print(count2)
