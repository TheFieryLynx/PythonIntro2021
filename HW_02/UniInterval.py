tuples = list(eval(input()))
tuples.sort(key=lambda x: x[0])

cur_min = -1
cur_max = -1

S = 0

for tup in tuples:
    if tup[0] <= cur_max and tup[1] > cur_max:
        cur_max = tup[1]
    elif tup[0] > cur_max:
        S += cur_max - cur_min
        cur_min = tup[0]
        cur_max = tup[1]

S += cur_max - cur_min
print(S)