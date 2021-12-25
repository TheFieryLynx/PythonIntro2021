task = ''
while True:
	rule = input().split()
	if len(rule[0]) > 1:
		tmp = ''
		for i in list(rule[0]):
			tmp += f'{i},'
		task += f"class pepelaC3({tmp[:-1]}):\n"
		if len(rule) == 3:
			for i in list(rule[1]):
				task += f"\t{i} = '{i}'\n"
			task += f"\tdef __init__(self):\n"
			task += f"\t\tfor i in '{rule[2]}':\n"
		else:
			task += f"\tdef __init__(self):\n"
			task += f"\t\tfor i in '{rule[1]}':\n"
			
		task += f"\t\t\tif i not in dir(self):\n"
		task += f"\t\t\t\traise Exception\n"
		task += f"pepelaC3()"
		break
	
	if len(rule) == 1:
		task += f"class {rule[0]}:\n"
		task += "\tpass\n"
	
	if len(rule) == 2:
		if rule[1].islower():
			task += f"class {rule[0]}:\n"
			for i in list(rule[1]):
				task += f"\t{i} = '{i}'\n"
		else:
			tmp = ''
			for i in list(rule[1]):
				tmp += f'{i},'
			task += f"class {rule[0]}({tmp[:-1]}):\n"
			task += '\tpass\n'
			
	if len(rule) == 3:
		tmp = ''
		for i in list(rule[1]):
			tmp += f'{i},'
		task += f"class {rule[0]}({tmp[:-1]}):\n"
		for i in list(rule[2]):
			task += f"\t{i} = '{i}'\n"
print(task)
try:
	exec(task)
	print("Correct")
except Exception:
	print("Incorrect")