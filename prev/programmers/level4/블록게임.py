# 1. 검은 돌을 채울 수 없는 공간(컬러 블록 밑)을 -1로 초기화한다.
# 2. 배열에 컬러 블록의 위치를 기록한다. (왼쪽 위, 오른쪽 아래 좌표)
# 3. 2.의 배열을 순회하면서 제거될 수 있는 블록이 없을 때까지 제거한다.
#    -> 1. 컬러 블록의 좌표 내 직사각형의 모든 원소가 0이거나 컬러블록의 숫자와 같으면 제거할 수 있다.
#    -> 2. 블록이 제거되면 해당 공간을 0으로 채우고 배열의 맨 하단 또는 다른 블록을 만날 때 까지 0으로 변경한다.
class Block:
    def __init__(self, value):
        self.value = value
        self.r1, self.c1, self.r2, self.c2 = 50, 50, 0, 0
        self.removed = False

    def update_pts(self, row, col):
        self.r1 = min(self.r1, row)
        self.c1 = min(self.c1, col)
        self.r2 = max(self.r2, row)
        self.c2 = max(self.c2, col)

    def remove(self, board):
        for r in range(self.r1, self.r2 + 1):
            for c in range(self.c1, self.c2 + 1):
                if board[r][c] != self.value and board[r][c] != 0:
                    return False
        self.update_board(board)
        self.removed = True
        return True

    def update_board(self, board):
        for c in range(self.c1, self.c2 + 1):
            flag = False
            for r in range(0, len(board)):
                if board[r][c] > 0 and board[r][c] != self.value:
                    flag = True
                elif flag: board[r][c] = -1
                else: board[r][c] = 0


direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]


def solution(board):
    blocks = get_blocks(board)
    answer = 0
    while True:
        flag = False
        for block in blocks:
            if not block.removed and block.remove(board):
                flag, answer = True, answer + 1
        if not flag: break
    return answer


def get_blocks(board):
    blocks = []
    visited = [[False for _ in range(len(board))] for _ in range(len(board))]
    for col in range(len(board)):
        flag = False
        for row in range(len(board)):
            if board[row][col] > 0:
                if not visited[row][col]:
                    block = Block(board[row][col])
                    update_block(board, visited, row, col, block)
                    blocks.append(block)
                flag = True
            elif flag:
                board[row][col] = -1
            visited[row][col] = True
    return blocks


def update_block(board, visited, row, col, block):
    block.update_pts(row, col)
    visited[row][col] = True
    for i in range(4):
        n_row = row + direction[i][0]
        n_col = col + direction[i][1]
        if n_row < 0 or n_col < 0 or n_row >= len(board) or n_col >= len(board):
            continue
        if visited[n_row][n_col] or board[n_row][n_col] != block.value:
            continue
        update_block(board, visited, n_row, n_col, block)


print(solution([
    [4,4,0,0,0,0],
    [4,1,0,0,5,5],
    [4,1,0,0,0,5],
    [0,1,1,0,2,5],
    [0,3,0,0,2,0],
    [3,3,3,0,2,2],
    ]))