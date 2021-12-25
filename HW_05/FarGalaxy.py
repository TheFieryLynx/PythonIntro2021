import math
inp = input().split()
d = {}
while len(inp) > 1:
	d[(float(inp[0]), float(inp[1]), float(inp[2]))] = inp[3]
	inp = input().split()

dist = 0
gal1 = ''
gal2 = ''

for k1, v1 in d.items():
	for k2, v2 in d.items(): 
		if k1 != k2:
			dist_tmp = math.sqrt((k1[0] - k2[0]) ** 2 + (k1[1] - k2[1]) ** 2 + (k1[2] - k2[2]) ** 2)
			if dist_tmp > dist:
				dist = dist_tmp
				gal1 = v1
				gal2 = v2

lst = sorted([gal1, gal2])
print(lst[0], lst[1])