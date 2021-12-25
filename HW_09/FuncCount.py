from functools import wraps

def counter(func):
	func.counter = lambda: wrapper.cnt
	@wraps(func)
	def wrapper(*args, **kwargs):
		wrapper.cnt += 1		
		return func(*args, **kwargs)
	wrapper.cnt = 0
	return wrapper