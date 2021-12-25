class DivStr(str):
	
	def to_DivStr(i):
		f = str.__dict__[i]
		def func(*args):
			ret = f(*args)
			if isinstance(ret, str):
				return DivStr(ret)
		func.__name__ = i
		return func
	
	for i in str.__dict__:
		if i[0:2] != '__' or i in ('__getitem__', '__add__', '__mul__', '__rmul__'):
			if callable(str.__dict__[i]):
				locals()[i] = to_DivStr(i)
		
	def __init__(self, inp):
		self.str = inp
		
	def __str__(self):
		return self.str
	
	def __floordiv__(self, other):
		length = len(self.str) // other
		rem = len(self.str) - other * length
		ret = []
		for i in range(other):
			ret.append(DivStr(self.str[0 + i * length:length + i * length]))
		return ret
		
	def __mod__(self, other):
		length = len(self.str)
		a = length % other
		return DivStr(self.str[length - a:])
	