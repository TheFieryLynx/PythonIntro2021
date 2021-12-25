import math
class Triangle:
	
	def __init__(self, a, b, c):
		self.isEmpty = False
		self.a = float(a)
		self.b = float(b)
		self.c = float(c)
		if (a > b + c or b > a + c or c > a + b):
			self.isEmpty = True
			
	def __str__(self):
		return f'{self.a}:{self.b}:{self.c}'
	
	def __abs__(self):
		if self.isEmpty:
			return float(0)
		else:
			p = (self.a + self.b + self.c)/2   
			s = math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
			return s
	def __bool__(self):
		return not self.isEmpty
	# x < y
	def __lt__(self, other):
		return abs(self) < abs(other)
	# x <= y
	def __le__(self, other):
		return abs(self) <= abs(other)
	# x == y
	def __eq__(self, other):
		if self.a == other.a:			
			if self.b == other.b:			#(a,b,c)(a,b,c)
				if self.c == other.c:
					return True
			if self.b == other.c:			#(a,b,c)(a,c,b)
				if self.c == other.b:
					return True
		
		if self.a == other.b:				
			if self.b == other.a:			#(a,b,c)(b,a,c)
				if self.c == other.c:
					return True
			if self.b == other.c:			#(a,b,c)(b,c,a)
				if self.c == other.a:
					return True
		
		if self.a == other.c:
			if self.b == other.a:			#(a,b,c)(c,a,b)
				if self.c == other.b:
					return True
			if self.b == other.b:			#(a,b,c)(c,b,a)
				if self.c == other.a:
					return True
		return False
	
	# x != y
	def __ne__(self, other):
		return not (self == other)
	# x > y
	def __gt__(self, other):
		return abs(self) > abs(other)
	
	# x >= y
	def __ge__(self, other):
		return abs(self) >= abs(other)
	
tri = Triangle(3, 4, 5), Triangle(5, 4, 3), Triangle(7, 1, 1), Triangle(5, 5, 5), Triangle(7, 4, 4)
for a, b in zip(tri[:-1], tri[1:]):
	print(a if a else b)
	print(f"{a}={abs(a):.2f} {b}={abs(b):.2f}")
	print(a == b)
	print(a >= b)
	print(a < b)