import itertools
def chainslice(begin, end, *args):
	yield from itertools.islice(itertools.chain(*args), begin, end)

print(*(chainslice(17, 33, range(7),  range(8),  range(6),  range(9),  range(5))))