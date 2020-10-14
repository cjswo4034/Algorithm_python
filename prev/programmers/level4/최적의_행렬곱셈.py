def solution(matrix_sizes):
    mem = [[0 for _ in range(len(matrix_sizes))] for _ in range(len(matrix_sizes))]
    return dq(matrix_sizes, mem, 0, len(matrix_sizes) - 1)


def dq(matrix, mem, l, r):
    if l == r: return 0
    if mem[l][r]: return mem[l][r]

    mem[l][r] = 987654321
    for i in range(l, r):
        mem[l][r] = min(mem[l][r], dq(matrix, mem, l, i) + dq(matrix, mem, i + 1, r) + matrix[l][0] * matrix[i][1] * matrix[r][1])

    return mem[l][r]


print(solution([[3, 2], [2, 4], [4, 1]]))
print(solution([[20, 1], [1, 30], [30, 10], [10, 10]]))