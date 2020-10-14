def solution(n):
    answer = [0]
    for i in range(1, n):
        answer = answer + [0] + [i ^ 1 for i in answer[::-1]]
    return answer


print(solution(4))