class Tester:

	def __init__(self, f):
		self.fun = f
		
	def __call__(self, suite, *allowed):
		saved_ex = []
		for i in suite:
			try:
				self.fun(*i)
			except Exception as exception:
				saved_ex.append(type(exception))
		if len(saved_ex) == 0:
			return 0
		if (len(allowed) == 0 and len(saved_ex) != 0):
			return 1
		if len(allowed) != 0 and Exception not in allowed[0]:
			for i in saved_ex:
				if i not in allowed[0]:
					return 1
		return -1
