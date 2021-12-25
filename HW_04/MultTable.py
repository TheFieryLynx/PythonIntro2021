import math
def print_horiz_line(M):
	print ('=' * M)

N, M = map(int, input().split(','))

column_width = len(str(N)) * 2 + len(str(N * N)) + 7
row_len = M // column_width
row_num = math.ceil(N / row_len)

while column_width * row_len + (row_len - 1) * 2 > M:
	row_len -= 1
	row_num = math.ceil(N / row_len)

table = [['.' for i in range(N + 1)] for j in range(N + 1)]
for i in range (1, N + 1):
	for j in range (1, N + 1):
		table[i][j] = f"{i:>{len(str(N))}} * {j:<{len(str(N))}} = {i*j:<{len(str(N * N))}} "

print_horiz_line(M)
for line in range(0, row_num):
	for i in range(1, N + 1):
		s = ''
		right_corner = row_len * (line + 1)
		if line == row_num - 1 and right_corner > N:
			right_corner = N - (N // row_len) * row_len + row_len * line
			
		for j in range(1 + line * row_len, right_corner + 1):
			s += table[j][i]
			if j != right_corner:
				s += '| '
		
		print(s)
	print_horiz_line(M)
