def solution(board):
    answer = 0
    fill_black(board)
    while True:
        cnt = find(board)
        if cnt: answer += cnt
        else: return answer
        fill_black(board)

def fill_black(board):
    for col in range(len(board)):
        row = 0
        while row < len(board) and board[row][col] < 1:
            board[row][col] = -1
            row += 1

def find(board):
    res = 0
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] > 0 and removeable(board, r, c, [[r, c]]): res += 1
    return res

def removeable(board, r, c, visit):
    res, q = [[r, c], [r, c]], [[r, c]]
    while q:
        current = q.pop(0)
        for d in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
            nr = current[0] + d[0]
            nc = current[1] + d[1]
            if nr < 0 or nc < 0 or nr >= len(board) or nc >= len(board): continue
            if [nr, nc] in visit: continue
            if board[nr][nc] == board[r][c]:
                visit.append([nr, nc])
                q.append([nr, nc])
                res[0] = [min(res[0][0], nr), min(res[0][1], nc)]
                res[1] = [max(res[1][0], nr), max(res[1][1], nc)]
    return remove(board, res, board[r][c])

def remove(board, arr, color):
    for r in range(arr[0][0], arr[1][0] + 1):
        for c in range(arr[0][1], arr[1][1] + 1):
            if not (board[r][c] == color or board[r][c] == -1): return False
    for r in range(arr[0][0], arr[1][0] + 1):
        for c in range(arr[0][1], arr[1][1] + 1):
            board[r][c] = 0
    return True
                

print(solution([
    [0, 1, 0, 0, 0, 0, 0, 5, 0, 0], 
    [0, 1, 0, 2, 2, 0, 0, 5, 5, 5], 
    [1, 1, 0, 2, 3, 0, 0, 0, 0, 0], 
    [0, 0, 0, 2, 3, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 3, 3, 4, 0, 0, 0], 
    [0, 6, 0, 0, 0, 4, 4, 0, 0, 0], 
    [6, 6, 6, 0, 3, 0, 4, 0, 0, 0], 
    [0, 0, 0, 2, 3, 0, 0, 0, 5, 5], 
    [1, 2, 2, 2, 3, 3, 0, 0, 0, 5], 
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 5]]))

# c: 1, n: 0(불가능)
# [t] t f 
# c: 1, n: 1
# [f] f f
# c: 1, n: -1
# [f] t t
# c: 1, n: 2
# [t] t f