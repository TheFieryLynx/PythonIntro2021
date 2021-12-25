a = int(input())
if a % 10 == 0:
	print('NO')
else:
	tmp = a
	new_number = 0
	while a != 0:
		new_number = new_number * 10 + a % 10
		a //= 10

	if tmp == new_number:
		print ('YES')
	else: 
		print('NO')