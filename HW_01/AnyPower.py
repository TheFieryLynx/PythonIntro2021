def check_degree(i, n):
	j = i * i
	while j < n:
		j *= i
	if j != n:
		return False
	else: 
		return True

N = int(input())

if N > 1000000 or N < 2:
	print ('NO')
elif N % 2 == 0:
	for i in range(2, 1001, 2):
		check = check_degree(i, N)
		if check:
			break
else:
	for i in range(3, 1001, 2):
		check = check_degree(i, N)
		if check:
			break

if check:
	print('YES')
else:
	print('NO')