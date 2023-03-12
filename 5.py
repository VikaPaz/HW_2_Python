max_n = int(input())
count = 1
while (i := int(input())) != 0:
    if i == max_n:
        count += 1
    elif i > max_n:
        count = 1
        max_n = i
print(count)
