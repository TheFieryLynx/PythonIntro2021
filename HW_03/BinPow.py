def BinPow(a, n, f):
	if n == 1:
		return a
	if n % 2 == 1:
		return f(BinPow(a, n - 1, f), a)
	else:
		b = BinPow(a, n // 2, f)
		return f(b, b)

def BinPow2(a, n, f):
	res = a
	n -= 1
	while n:
		if n & 1:
			res = f(res, a)
		a = f(a, a)
		print(n, a, res)
		n >>= 1
	return res

print(BinPow(2,33, int.__mul__), 2**33)
print(BinPow2("Se", 11, str.__add__))