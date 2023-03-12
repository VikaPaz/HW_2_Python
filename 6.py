n = int(input())
sum_f = 0
f = 1
while n > 0:
    f *= n
    n -= 1
    sum_f += f + 1
print(sum_f)
