def solution(weights):
    weights.sort()
    answer, total = sum(weights) + 1, 1

    for weight in weights:
        if total < weight:
            answer = total
            break
        total += weight

    return answer


print(solution([3, 1, 6, 2, 7, 30, 1]))
print(solution([1, 2, 4, 8]))