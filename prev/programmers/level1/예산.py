def solution(d, budget):
    if sum(d) <= budget: return len(d)
    d.sort()
    answer = 0
    for cost in d:
        budget -= cost
        if budget < 0: break
        answer += 1

    return answer


print(solution([1, 3, 2, 5, 4], 9))
print(solution([2, 2, 3, 3], 10))
