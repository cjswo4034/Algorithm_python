def BFS(arr, visited, r, c, curr):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    stack = [[0, 0, 1, 0]]
    while stack:
        x, y, d, m = stack.pop()
        if arr[x][y] == '@':
            return True
        if visited[x][y][d][m] == curr:
            continue
        else:
            visited[x][y][d][m] = curr
            qm = False
            if arr[x][y] == '<' or (arr[x][y] == '_' and m is not 0):
                d = 0
            elif arr[x][y] == '>' or (arr[x][y] == '_' and m is 0):
                d = 1
            elif arr[x][y] == '^' or (arr[x][y] == '|' and m is not 0):
                d = 2
            elif arr[x][y] == 'v' or (arr[x][y] == '|' and m is 0):
                d = 3
            elif arr[x][y] == '?':
                qm = True
            elif arr[x][y] == '+':
                m = (m + 1) % 16
            elif arr[x][y] == '-':
                m = (m - 1) % 16
            elif arr[x][y] is not '.':
                m = int(arr[x][y])

            if qm:
                stack.extend([[(x + dx[i]) % r, (y + dy[i]) % c, i, m] for i in range(4)])
            else:
                stack.append([(x + dx[d]) % r, (y + dy[d]) % c, d, m])
    return False


T = int(input())
check = [[[[[0] for _ in range(16)] for _ in range(4)] for _ in range(20)] for _ in range(20)]
for test_case in range(1, T + 1):
    R, C = map(int, input().split())
    arr = [input() for _ in range(R)]

    answer = 'YES' if BFS(arr, check, R, C, test_case) else 'NO'
    print(f'#{test_case} {answer}')
