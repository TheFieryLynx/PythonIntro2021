import random
import itertools

def randomes(seq):
	for a, b in itertools.cycle([tuple(i) for i in seq]):
		yield random.randint(a, b)
