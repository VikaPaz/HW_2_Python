x = int(input())
if x >= 2:
	for i in range(2, x):
		if x % i == 0:
			print(i)
			break
else:
	print("ERROR")