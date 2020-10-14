def solution(m, n, board):
    board = [[ord(el) for el in row] for row in board]
    removable_block = find_removable_block(board)

    while removable_block:
        remove(board, removable_block)
        arrange_board(board)
        removable_block = find_removable_block(board)

    return sum([row.count(-1) for row in board])

def find_removable_block(board):
    res = []
    for r in range(len(board) - 1):
        for c in range(len(board[0]) - 1):
            if board[r][c] == -1: continue
            if board[r][c] == board[r + 1][c] == board[r][c + 1] == board[r + 1][c + 1]:
                res.append([r, c])
    return res

def remove(board, removable_block):
    for r, c in removable_block:
        board[r][c] = board[r + 1][c] = board[r][c + 1] = board[r + 1][c + 1] = -1

def arrange_board(board):
    # 각 열의 마지막 행부터 탐색한다.
    # 탐색중인 행의 원소가 X라면 정지하고 다음 행부터 X가 아닌 문자를 찾는다.
    # X가 아닌 문자를 찾으면) 그 문자를 맨 아래 X의 위치에 저장하고 문자의 원래 위치는 X로 채운다.
    # X가 아닌 문자를 못찾으면) 넘어간다.
    for c in range(len(board[0])):
        for r in range(len(board) - 1, -1, -1):
            if board[r][c] == -1:
                runner = r - 1
                while runner >= 0 and board[runner][c] == -1:
                    runner -= 1
                if runner >= 0 and board[runner][c] != -1:
                    board[r][c], board[pos][c] = board[runner][c], -1

# 지울 블록을 표시한다.
# 지울 블록이 있다면)
#   1. 표시된 블록을 지운다. (X 표시)
#   2. 지운 블록의 개수를 더한다.
#   3. 블록을 밑으로 내린다.
# 지울 블록이 없다면)
# 지운 블록들의 개수를 반환한다.