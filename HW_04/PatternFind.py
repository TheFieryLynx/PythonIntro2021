string = input()
temp = input()

for i in range(len(string) - len(temp) + 1):
	for j in range(len(temp)):
		if temp[j] != '@':
			if temp[j] != string[j + i]:
				break
	else:
		print(i)
		break
else:
	print(-1)
	
		
		