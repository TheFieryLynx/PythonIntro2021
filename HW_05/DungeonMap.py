caves = {}
inp = input().split()
while len(inp) > 1:
	if inp[0] in caves:
		caves[inp[0]].add(inp[1])
	else:
		caves[inp[0]] = {inp[1]}
		
		
	if inp[1] in caves:
		caves[inp[1]].add(inp[0])	
	else:
		caves[inp[1]] = {inp[0]}
		
	inp = input().split()
	
in_ = inp[0]
out_ = input()

tun_set = {in_}

tun_len_1 = len(tun_set)
tun_len_2 = 0

while True:
	new_set = set()
	for i in tun_set:
		new_set.update(caves[i])
		if out_ in caves[i]:
			break
	tun_set.update(new_set)
	tun_len_2 = len(tun_set)
	if tun_len_1 == tun_len_2:
		break
	tun_len_1 = tun_len_2

if out_ in tun_set:
	print('YES')
else:
	print('NO')
	
	