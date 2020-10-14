def solution(A, B):
    if min(A) >= max(B): return 0
    answer = 0
    A = sorted(A)
    B = sorted(B)
    while A:    # 배열 순회가 더 빠름
        curr = A.pop(0)
        while B:
            if B.pop(0) > curr:
                answer += 1
                break
    return answer

# 2345
# 1234
print(solution([5,1,3,7], [2,2,6,8]))
print(solution([2,2,2,2], [1,1,1,1]))
