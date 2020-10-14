import math


def solution(w, h):
    if w == 1 or h == 1: return 0
    if w == h: return w * w - w
    answer = w * h

    slope = max(w, h) / min(w, h)
    for i in range(1, min(w, h) + 1):
        print(answer, math.ceil(slope * i), math.floor(slope * (i - 1)))
        answer -= (math.ceil(slope * i) - math.floor(slope * (i - 1)))

    return answer


print(solution(4, 5))