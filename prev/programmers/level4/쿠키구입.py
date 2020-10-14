from itertools import accumulate
answer = 0


def solution(cookie):
    global answer
    for m in range(len(cookie)-1):
        a = set(accumulate(reversed(cookie[:m+1])))
        b = set(accumulate(cookie[m+1:]))
        c = a & b

        if c: answer = max(*c, answer)
    return answer


def solution2(cookies):
    largest = set()
    for m in range(1, len(cookies)):
        l, r = 0, 0
        ls = set()
        for i in range(m-1, -1, -1):
            l += cookies[i]
            ls.add(l)
        for i in range(m, len(cookies)):
            r += cookies[i]
            if r in ls:
                largest.add(r)
    return max(largest) if largest else 0


# 무식하게 풀기
def solution1(cookies):
    for divider in range(1, len(cookies)):
        helper1(cookies, divider - 1, 0, divider, 0)
    return answer


def helper1(cookies, l, l_sum, r, r_sum):
    if l_sum == r_sum:
        global answer
        answer = max(answer, l_sum)
    if l < 0 or r >= len(cookies): return
    helper1(cookies, l - 1, l_sum + cookies[l], r, r_sum)
    helper1(cookies, l, l_sum, r + 1, r_sum + cookies[r])


print(solution1([1,1,2,3]))
print(solution1([1,2,4,5]))
