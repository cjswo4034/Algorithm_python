def solution(stones, k):
    answer = 0
    l, r = 0, 200_000_000
    while l <= r:
        mid, length, tmp = (l + r) >> 1, 0, 0
        for i in range(len(stones)):
            if stones[i] <= mid:
                tmp += 1
            else:
                length = max(length, tmp)
                tmp = 0
        else:
            length = max(length, tmp)

        if length >= k:
            answer = mid
            r = mid - 1
        else:
            l = mid + 1

    return answer


def solution2(stones, k):
    answer = 0
    l, r = 0, 200_000_000
    while l <= r:
        mid = (l + r) >> 1
        if possible_jump(stones, k, mid):
            answer = mid
            l = mid + 1
        else:
            r = mid - 1
    return answer


def possible_jump(stones, k, value):
    count = k
    for stone in stones:
        if stone < value:
            count -= 1
        else:
            count = k
        if count == 0:
            return False
    return True


print(solution2([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))
print(solution2([5, 5, 5, 5, 5], 5))