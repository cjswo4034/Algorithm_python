def solution(m, n, board):
    answer = 0
    board = convert_int_board(board)

    while True:
        count = scan(board)
        if count < 1: break
        answer += count
        arrange_board(board)
        for row in board:
            print(row)

    return answer


def arrange_board(board):
    for i in range(len(board) - 1, 0, -1):
        for j in range(len(board[0])):
            if board[i][j] != -1: continue
            k = i - 1
            while k >= 0 and board[k][j] == -1:
                k -= 1
            if k >= 0:
                board[i][j] = board[k][j]
                board[k][j] = -1


def convert_int_board(board):
    return [[ord(board[i][j]) - ord('A') for j in range(len(board[0]))] for i in range(len(board))]


def scan(board):
    count, visit = 0, []
    for i in range(len(board) - 1):
        for j in range(len(board[0]) - 1):
            if board[i][j] == -1: continue
            count += removable_idx(board, visit, i, j)
    for i in visit:
        board[i[0]][i[1]] = -1
    return count


def removable_idx(board, visited, x, y):
    ret_cnt, ret_visit = 0, []
    criterion = board[x][y]
    for i in range(2):
        for j in range(2):
            if criterion != board[x + i][y + j]: return 0
            if [x + i, y + j] in visited: continue
            ret_cnt += 1
            ret_visit.append([x + i, y + j])
    visited.extend(ret_visit)
    return ret_cnt


print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))
print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))