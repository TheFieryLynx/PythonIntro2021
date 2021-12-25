import itertools

class Dots:
	
	def __init__(self, a, b):
		self.a = a
		self.b = b
		
	def gen(self, start, stop, step):
		for i in range(start, stop):
			yield self.a + i * step
		
	def __getitem__(self, item):
		if isinstance(item, slice):
			if item.step == None:
				return float(self.a) + item.start * (self.b - self.a) / (item.stop - 1)
			else:
				start_pos = 0 if item.start == None else item.start
				stop_pos = item.step if item.stop == None else item.stop
				return self.gen(start_pos, stop_pos, (self.b - self.a) / (item.step - 1))
		else:
			return self.gen(0, item, (self.b - self.a) / (item - 1))
		
