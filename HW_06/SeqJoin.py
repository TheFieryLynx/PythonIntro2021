import itertools

def find_min(ind, args):
	check = True
	cur_min = ''
	cur_min_i = -1
	for i, j in enumerate(ind):
		if j != -1 and check:
			cur_min = args[i][j]
			cur_min_i = i
			check = False
		elif j != -1 and not check:
			if args[i][j] < cur_min and cur_min_i != i:
				cur_min = args[i][j]
				cur_min_i = i
	return cur_min_i, cur_min

def joinseq(*args):
	indexes = [0] * len(args)
	its = [iter(i) for i in args]
	for it in its:
		next(it)
	while True:
		i, cur_min = find_min(indexes, args)
		if i != -1:
			ret_next = next(its[i], 'STOP')
			if ret_next == 'STOP':
				indexes[i] = -1
			else:
				indexes[i] += 1
		else:
			break
		yield cur_min
	
print("".join(joinseq("abs", "qr", "azt")))