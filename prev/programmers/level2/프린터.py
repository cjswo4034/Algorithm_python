def solution(priorities, location):
    ans = [0 for i in range(len(priorities))]
    idx = [i for i in range(len(priorities))]
    cnt = 1
    while priorities:
        if priorities[0] is not max(priorities):
            priorities.append(priorities[0])
            idx.append(idx[0])
        else:
            ans[idx[0]] = cnt
            cnt += 1
        del priorities[0]
        del idx[0]

    return ans[location]


print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))
