count = 0
for i in range(1, x := int(input()) + 1):
    if x % i == 0:
        count += 1
print(count)
