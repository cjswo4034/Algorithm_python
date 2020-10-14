""" ** 시간초과 **
# 6 -> 2x3 60, 2x1:4x1 12
# 1. 각 열의 1의 개수(col_cnt) 총합(n)을 짝수만으로 만들 수 있는 조합 구하기. 짝수는 열의 크기와 같거나 작다
# 2. 1.의 조합들에 대해서 col_cnt를 만들 수 있는 수 구하기
# 3. 각각의 2.에 대해서 (행의 크기)C(사용한 행의 개수) 의 총합 구하기
"""

"""
아예 모르겠음
https://programmers.co.kr/questions/13628
"""


def get_num_of_case_matrix(len_row):
    res = [[0 for _ in range(len_row + 1)] for _ in range(len_row + 1)]
    res[0][0] = 1
    for c in range(len_row + 1):
        for r in range(1, len_row + 1):
            temp1 = res[r - 1][c - 1] or 0
            temp2 = res[r - 1][c]
            res[r][c] = temp1 + temp2
    return res


def init_res_arr(row, col):
    """
    문제의 결과를 구하는데 사용항 dp matrix를 초기화한다.
    matrix[i][j] = i열에서 j개의 짝수 행을 만드는 경우의 수
    :param row: 행렬의 행의 크기
    :param col: 행렬의 열의 크기
    :return:    dp Matrix
    """
    res = [[0] * (row + 1) for _ in range(col + 1)]
    res[0][row] = 1
    return res


def get_num_of_col(a, col):
    """
    a[:][column] 의 1의 개수
    :return: 1의 개수
    """
    return sum([a[row][col] for row in range(len(a))])


def get_num_of_case(a, b, target, total, num_of_case_matrix):
    """ 주어진 개수의 1을 추가해서 짝수의 개수를 목표치 개수만큼 만들 수 있는 경우의 수를 구한다.
    :param a: 짝수의 개수
    :param b: 추가할 1의 개수
    :param target: 목표 짝수 개수
    :param total: 전체 개수
    :param num_of_case_matrix: 이전까지의 경우의 수
    :return: 경우의 수
    """
    over = (a + b - target) // 2    # 짝수에서 홀수로 바뀌는 행의 개수
    non_over = b - over             # 홀수에서 짝수로 바뀌는 행의 개수

    over_num = num_of_case_matrix[a][over]                  # 짝수인 행에서 홀수로 변하는 행을 선택하는 경우의 수
    non_over_num = num_of_case_matrix[total - a][non_over]  # 홀수인 행에서 짝수로 변하는 행을 선택하는 경우의 수

    return over_num * non_over_num  # 전체 경우의 수


def solution(a):
    """
    :param a: 주어진 2차원 배열
    :return: 정답
    """
    ans, DIV = -1, int(1e7 + 17)
    len_row = len(a)
    len_col = len(a[0])
    
    num_of_case_matrix = get_num_of_case_matrix(len_row)
    res_dp_matrix = init_res_arr(len_row, len_col)  # i개의 열을 충족시켰을 때, j개의 짝수 행을 만드는 경우의 수

    for i in range(1, len_col + 1):
        cnt = get_num_of_col(a, i - 1)              # 현재 열에서 사용해야하는 1의 개수
        for j in range(len_row + 1):
            s = abs(cnt - j)
            e = min(cnt + j, len_row)

            for k in range(s, e + 1, 2):
                num = get_num_of_case(k, cnt, j, len_row, num_of_case_matrix)
                res_dp_matrix[i][j] = (res_dp_matrix[i][j] + num * res_dp_matrix[i - 1][k]) % DIV

    for row in res_dp_matrix:
        print(row)
    return res_dp_matrix[-1][-1]


a = [[1,0,0,1,1],[0,0,0,0,0],[1,1,0,0,0],[0,0,0,0,1]]
print(solution(a))

# print(sum((2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100, 102, 104, 106, 108, 110, 112, 114, 116, 118, 120, 122, 124, 126, 128, 130, 132, 134, 136, 138, 140, 142, 144, 146, 148, 150, 152, 154, 156, 158, 160, 162, 164, 166, 168, 170, 172, 174, 176, 178, 180, 182, 184, 186, 188, 190, 192, 194, 196, 198, 200, 202, 204, 206, 208, 210, 212, 214, 216, 218, 220, 222, 224, 226, 228, 230, 232, 234, 236, 238, 240, 242, 244, 246, 248, 250, 252, 254, 256, 258, 260, 262, 264, 266, 268, 270, 272, 274, 276, 278, 280, 282, 284, 286, 288, 290, 292, 294, 294, 294, 294, 294, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 298, 298, 298, 298, 298, 298, 298, 298, 298, 298, 298, 298, 298, 298, 298, 298, 298, 298, 298, 298, 298, 298, 298, 298, 298, 298, 298, 298, 298, 298, 298, 298, 298, 298, 298, 298, 298, 298, 298, 298, 298, 298, 298, 298, 298, 298, 298, 298, 298, 298, 298, 298, 298, 298, 298, 298, 298, 298, 298, 298, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300)))
# print(len((2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100, 102, 104, 106, 108, 110, 112, 114, 116, 118, 120, 122, 124, 126, 128, 130, 132, 134, 136, 138, 140, 142, 144, 146, 148, 150, 152, 154, 156, 158, 160, 162, 164, 166, 168, 170, 172, 174, 176, 178, 180, 182, 184, 186, 188, 190, 192, 194, 196, 198, 200, 202, 204, 206, 208, 210, 212, 214, 216, 218, 220, 222, 224, 226, 228, 230, 232, 234, 236, 238, 240, 242, 244, 246, 248, 250, 252, 254, 256, 258, 260, 262, 264, 266, 268, 270, 272, 274, 276, 278, 280, 282, 284, 286, 288, 290, 292, 294, 294, 294, 294, 294, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 296, 298, 298, 298, 298, 298, 298, 298, 298, 298, 298, 298, 298, 298, 298, 298, 298, 298, 298, 298, 298, 298, 298, 298, 298, 298, 298, 298, 298, 298, 298, 298, 298, 298, 298, 298, 298, 298, 298, 298, 298, 298, 298, 298, 298, 298, 298, 298, 298, 298, 298, 298, 298, 298, 298, 298, 298, 298, 298, 298, 298, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300)))