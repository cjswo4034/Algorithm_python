def solution(n, costs):
    union = [-1] * (n + 1)
    costs.sort(key=lambda x: x[2], reverse=True)

    ans, cnt = 0, 0
    while costs:
        curr = costs.pop()
        if merge(union, curr[0], curr[1]):
            costs.append(curr)
            ans += curr[2]
            cnt += 1
        if cnt + 1 >= n:
            break

    return ans


def merge(union, a, b):
    a_, b_ = find(union, a), find(union, b)
    if a_ == b_:
        return False
    union[b_] = a_
    return True


def find(union, a):
    if union[a] == -1:
        return a
    union[a] = find(union, union[a])
    return union[a]


print(solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]))
