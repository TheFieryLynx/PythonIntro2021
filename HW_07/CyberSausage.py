import fractions as fr

class Sausage():
	
	def __init__(self, *args):
		self.len = 12
		self.size = fr.Fraction('1')
		
		if len(args) == 0:
			self.meat = "pork!"
			
		if len(args) == 1:
			self.meat = args[0]
		
		if len(args) == 2:
			self.meat = args[0]
			self.size = fr.Fraction(args[1])
		
	def __str__(self):
		
		sz = self.size.as_integer_ratio()
		if (sz[0] == sz[1]):
			str = ''
			str += '/' + 12 * '-' + '\\' + '\n'
			ln = len(self.meat)
			rem = self.len % ln
			div = self.len // ln
			for i in range(3):
				str += '|' + self.meat * div + self.meat[0:rem] +'|' + '\n'
			str += '\\' + 12 * '-' + '/'
			return str
		if (sz[0] > sz[1]):
			n_div = sz[0] // sz[1]
			n_rem = sz[0] % sz[1]
			delta_len = self.len * n_rem // sz[1]
			
			str = ''
			str += ('/' + 12 * '-' + '\\') * n_div
			if (delta_len != 0):
				str += '/' + delta_len * '-' + '|'
			str += '\n'
			ln = len(self.meat)
			rem = self.len % ln
			div = self.len // ln
			
			delta_rem = delta_len % ln
			delta_div = delta_len // ln
			
			for i in range(3):
				str += ('|' + self.meat * div + self.meat[0:rem] +'|') * n_div
				if (delta_len != 0):
					str += '|' + self.meat * delta_div + self.meat[0:delta_rem] +'|' 
				str += '\n'
			str += ('\\' + 12 * '-' + '/') * n_div
			if (delta_len != 0):
				str += '\\' + delta_len * '-' + '|'
			return str
		# sz[0] < sz[1]
		ln = len(self.meat)
		delta_len = self.len * sz[0] // sz[1]
		delta_rem = delta_len % ln
		delta_div = delta_len // ln
		str = ''
		str += '/' + delta_len * '-' + '|' + '\n'
		for i in range(3):
			str += ('|' + self.meat * delta_div + self.meat[0:delta_rem] +'|') + '\n'
		str += '\\' + delta_len * '-' + '|'
		return str
		
	def __add__(self, other):
		return Sausage(self.meat, self.size + other.size)
	
	def __sub__(self, other):
		if self.size < other.size:
			return Sausage(self.meat, 0)
		return Sausage(self.meat, self.size - other.size)
	
	def __rmul__(self, other):
		return Sausage(self.meat, self.size * other)
	
	def __mul__(self, other):
		return Sausage(self.meat, self.size * other)
	
	def __truediv__(self, other):
		return Sausage(self.meat, self.size / other)
		
	def __abs__(self):
		return self.size
	
	def __bool__(self):
		if self.size == 0:
			return False
		return True

a, b, c = Sausage(), Sausage("HAM", "5/6"), Sausage("SPAM.", 1.25)
print(a, b, c, sep='\n')
print(a + b + c, abs(a + b + c))
print(b * 2, 4 * c / 5, sep="\n")
d, e = 2 * b + a / 3 - 25 * c / 16, a - c
print(d, not d, abs(d))
print(e, not e, abs(e))