import decimal
import math

def pi():
	pi = 0
	pi_tmp = 1
	n = 0
	while abs(pi_tmp) > decimal.Decimal(10) ** (-2000):
		pi_tmp = ((-1) ** n) / decimal.Decimal((decimal.Decimal(3) ** n) * (2 * n + 1))
		pi += pi_tmp
		n += 1
	return decimal.Decimal(12) ** (decimal.Decimal(1 / 2)) * pi

A = int(input())
E = int(input())
	
decimal.getcontext().prec = E + 10
	
A = A * pi() / 200

sin = decimal.Decimal(0)
cos = decimal.Decimal(0)
sin_tmp = decimal.Decimal(1)
cos_tmp = decimal.Decimal(1)
n = 0
eps = decimal.Decimal(10) ** (-2000)
while abs(sin_tmp) > eps and abs(cos_tmp) > eps:
	sin_tmp = decimal.Decimal(A ** (2 * n + 1)) / decimal.Decimal(math.factorial(2 * n + 1))
	cos_tmp = decimal.Decimal(A ** (2 * n)) / decimal.Decimal(math.factorial(2 * n))
	if n & 1 == 1:
		sin -= sin_tmp
		cos -= cos_tmp
	else:
		sin += sin_tmp
		cos += cos_tmp
	n += 1

decimal.getcontext().prec = E
tang = decimal.Decimal(sin / cos)
print(tang)
