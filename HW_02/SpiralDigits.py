M, N = map(int, input().split(','))

matrix = [[0]*M for i in range(N)]
columnShift, number, cnt = 0, 0, 0

for startLine in range(0, min(N // 2 + 1, M // 2 + 1)):
    if (cnt != M * N):
        for i in range(M - columnShift):
            matrix[startLine][i + startLine] = number
            number = (number + 1) % 10
            cnt += 1

    if (cnt != M * N):
        for i in range(startLine + 1, N - startLine):
            matrix[i][- startLine - 1] = number
            number = (number + 1) % 10
            cnt += 1


    if (cnt != M * N):
        for i in range(startLine + 1, M - startLine):
            matrix[- startLine - 1][- i - 1] = number
            number = (number + 1) % 10
            cnt += 1

    if (cnt != M * N):
        for i in range(startLine + 1, N - (startLine + 1)):
            matrix[- i - 1][startLine] = number
            number = (number + 1) % 10
            cnt += 1
    
    columnShift+=2

for i in matrix:
    print(*i)




























