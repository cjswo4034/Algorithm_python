# 1. idx를 인자로 받아 해당 위치의 제일 위쪽 인형을 stack에 옮긴다.
# 2. stack의 peek가 옮긴 인형과 동일하면 제거한다.
def solution1(board, moves):
    answer = 0
    stack = []
    for move in moves:
        row = find(board, move - 1)
        if row == -1: continue
        answer += remove(board, stack, row, move - 1)
    return answer


# 1. board의 각 열에 대해서 원소가 0이 아닌 가장 큰 행의 index를 구한다.
# 2. moves를 순회하며 해당 행과 열을 stack에 옮긴다.
# 3. 인형이 동일하면 제거한다.
def solution2(board, moves):
    answer = 0
    moves = [move - 1 for move in moves]
    idx, stack = [find(board, i) for i in range(len(board[0]))], []
    
    for move in moves:
        if idx[move] == len(board): continue
        answer += remove(board, stack, idx[move], move)
        idx[move] += 1
    return answer

# idx를 인자로 받고 해당 위치의 가장 위쪽 인형의 idx를 반환. 해당 열에 인형이 없으면 ret -1
def find(board, move):
    for row in range(len(board)):
        if board[row][move] != 0: return row
    return -1

# stack의 peek가 옮긴 인형과 동일하면 제거한다.
def remove(board, stack, row, col):
    target = board[row][col]
    board[row][col] = 0
    
    if stack and stack[-1] == target: 
        stack.pop()
        return 2
    else: 
        stack.append(target)
        return 0

print(solution2([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]	))