import itertools

def joinseq(*seq):
	print(*seq)
	print([i for i in itertools.chain(*seq)])
	print(sorted([i for i in itertools.chain(*seq)]))
	
	yield from sorted(itertools.chain(*seq))
	
print("".join(joinseq("abs", "qr", "azt")))