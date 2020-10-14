from collections import Counter
import heapq


class Car(object):
    def __init__(self, cnt, name):
        self.cnt = cnt
        self.name = name

    def __lt__(self, other):
        if self.cnt is not other.cnt: return self.cnt < other.cnt
        return self.name > other.name


def solution(votes, k):
    c = Counter(votes)
    q = [Car(v, k) for k, v in c.items()]
    tot, acc = sum([v for v in sorted(c.values())[-k:]]), 0

    heapq.heapify(q)

    prev, current = heapq.heappop(q), None
    acc = prev.cnt

    while q:
        current = heapq.heappop(q)

        acc += current.cnt
        if acc >= tot: break

        prev = current

    return prev.name


print(solution(["AVANT", "PRIDO", "SONATE", "RAIN", "MONSTER", "GRAND", "SONATE", "AVANT", "SONATE", "RAIN", "MONSTER", "GRAND", "SONATE", "SOULFUL", "AVANT", "SANTA"], 2))