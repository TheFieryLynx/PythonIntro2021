import math 

seq = set(eval(input()))

sum_set = set()

M = sorted(list(seq))[-1]
for i in range(1, int(math.sqrt(M)) + 1):
	for j in range(i, int(math.sqrt(M - i * i)) + 1):
		for k in range(j, int(math.sqrt(M - i * i - j * j)) + 1):
			sum_set.add(i * i + j * j + k * k)

print(len(seq.intersection(sum_set)))
