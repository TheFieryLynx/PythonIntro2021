import math

circle = list(map(float, input().split(',')))
point = list(map(float, input().split(',')))
while (point != [0, 0]):
	if math.hypot(point[0] - circle[0], point[1] - circle[1]) > circle[2]:
		print('NO')
		break;
	point = list(map(int, input().split(',')))
else:
	print('YES')