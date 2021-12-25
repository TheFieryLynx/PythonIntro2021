class WeAre:
	count = 0
	def __init__(self):
		type(self).count += 1
	def __del__(self):
		type(self).count -= 1
