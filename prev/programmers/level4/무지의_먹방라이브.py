def solution(food_times, k):    # 통과
    food_times = [[food_time, i] for i, food_time in enumerate(food_times)]
    food_times.sort()
    pos, lower, cnt = 0, 0, 0
    while pos < len(food_times):
        cnt = (food_times[pos][0] - lower) * (len(food_times) - pos)
        if k < cnt: break
        k, lower = k - cnt, food_times[pos][0]
        while pos < len(food_times) and lower == food_times[pos][0]:
            pos += 1

    if pos < len(food_times):
        res = sorted(food_times[pos:], key=lambda food_time: food_time[1])
        k = (k + len(res)) % len(res)
        return res[k][1] + 1
    return -1


# 개선2 적용 (효율 2개 통과)
def solution1(food_times, k):
    food_times = [[food_time, i] for i, food_time in enumerate(food_times)]
    food_times.sort()
    lower, cnt = 0, 0
    while food_times:
        tmp = food_times[0]
        cnt = (tmp[0] - lower) * len(food_times)
        if k < cnt: break
        k, lower = k - cnt, tmp[0]
        while food_times and tmp[0] == food_times[0][0]:
            food_times.pop(0)

    if food_times:
        food_times.sort(key=lambda food_time: food_time[1])
        k = (k + len(food_times)) % len(food_times)
        return food_times[k][1] + 1
    return -1


# 개선1 적용 (효율 통과 X)
def solution2(food_times, k):
    food_times = [[food_time, i] for i, food_time in enumerate(food_times)]
    while k > 0:
        if not food_times: return -1
        tmp = food_times.pop(0)
        tmp[0] -= 1
        if tmp[0] > 0:
            food_times.append(tmp)
        k -= 1
    if food_times: return food_times[0][1] + 1
    return -1


# 무작정 풀기
# 개선1: 1개 이상 남아있는 원소의 위치를 탐색하는 시간
# 개선2: food_time 을 1씩 제거하는 것
def solution3(food_times, k):
    pos = 0
    while k > 0:
        food_times[pos] -= 1
        while True:
            pos = (pos + 1) % len(food_times)
            if food_times[pos] > 0: break
            if max(food_times) <= 0: return -1
        k -= 1
    return pos + 1


import random

max_v = 100_000_000
test1 = [random.randint(1, max_v) for i in range(200000)]
print(solution([3, 1, 2], 5))
print(solution([3, 1, 2], 6))
print(solution1([3, 1, 2], 5))
print(solution1([3, 1, 2], 6))
# print(solution(test1, 2 * (10 ** 13)))