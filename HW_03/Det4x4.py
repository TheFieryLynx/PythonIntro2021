def det(matrix):
	permutations = []
	tmp = [-1] * 4
	used = 	[False] * 4
	
	def perm_gen(ind):
		if ind == 4:
			permutations.append(tmp.copy())
			return
		for i in [0, 1, 2, 3]:
			if not used[i]:
				tmp[ind] = i
				used[i] = True
				perm_gen(ind + 1)
				used[i] = False
				
	perm_gen(0)
	determinant = 0
	for i in permutations:
		inv = (i[0] > i[1]) + (i[0] > i[2]) + (i[0] > i[3]) + (i[1] > i[2]) + (i[1] > i[3]) + (i[2] > i[3])
		determinant += ((-1) ** inv) * matrix[0][i[0]] * matrix[1][i[1]] * matrix[2][i[2]] * matrix[3][i[3]]
			
	return determinant

m = list(eval(input()))
print(det(m))

			