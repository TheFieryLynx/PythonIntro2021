marine_chart = [list(input())]
inp = ''
cnt = 1
length = len(marine_chart[0])
while(inp != marine_chart[0]):
    inp = list(input())
    marine_chart.append(inp)
    cnt += 1

S = 0

for line in range(1, cnt - 1):
    for ch in range(1, length - 1):
        if marine_chart[line][ch] == '#':
            S += 1
            marine_chart[line][ch] = '0'
            if marine_chart[line + 1][ch] == '#':
                marine_chart[line + 1][ch] = '0'
            if marine_chart[line][ch + 1] == '#':
                marine_chart[line][ch + 1] = '0'

        elif marine_chart[line][ch] == '0':
            if marine_chart[line + 1][ch] == '#':
                marine_chart[line + 1][ch] = '0'
            if marine_chart[line][ch + 1] == '#':
                marine_chart[line][ch + 1] = '0'

print(S)