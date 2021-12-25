def squares(w, h, *args):
	res = [['.' for i in range(w)] for j in range(h)]
	for X, Y, s, c in args:
		for i in range(X, X + s):
			for j in range(Y, Y + s):
				res[j][i] = c
	for i in res:
		print(''.join(i))
