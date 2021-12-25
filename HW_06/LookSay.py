def LookSay():
    l = '1'
    s = 1
    y=''
    yield s
    while True:
        x = l + ' '
        for i in range(len(x) - 1):
            if x[i] == x[i + 1]:
                s += 1
            else:
                yield s
                yield int(x[i])
                y += str(s) + str(x[i])
                s = 1
        x = ''
        l = y
        y = ''
        s=1