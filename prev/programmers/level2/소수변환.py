def solution(nums):
    answer = 0
    eratos = get_eratos()
    for i in range(len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            for k in range(j + 1, len(nums)):
                value = nums[i] + nums[j] + nums[k]
                if not eratos[value]:
                    print(nums[i], nums[j], nums[k])
                    answer += 1
    return answer


def solution2(nums):
    from itertools import combinations as cbs
    answer = 0
    eratos = get_eratos()
    for cb in cbs(nums, 3):
        value = sum(cb)
        if not eratos[value]:
            answer += 1

    return answer


def get_eratos():
    import math
    eratos = [False] * 3001
    eratos[0] = eratos[1] = True
    for i in range(2, int(math.sqrt(3000) + 1)):
        if not eratos[i]:
            for j in range(i + i, 3001, i):
                eratos[j] = True
    return eratos


print(get_eratos())
print(solution2([1, 2, 7, 6, 4]))