def divdigit(n):
	tmp = n
	cnt = 0
	while n > 0:
		if n % 10 > 0 and tmp % (n % 10) == 0:
			cnt += 1
		n //= 10
	return cnt
			