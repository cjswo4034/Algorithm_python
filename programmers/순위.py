""" 
[Level 3] 순위
* B를 이길 수 있는 선수(A)는 B가 이길 수 있는 선수(C)도 이길 수 있다. (A -> B -> C) 
  -> Floyd
"""


def solution(n, results):
    """
    1. N + 1 크기를 갖는 2차원 배열을 초기화한다.
    2. A가 B를 이길 수 있으면 arr[A][B] -> True
    3. 0 <= B < N인 B에 대해서 A가 B를 이길 수 있고 B가 C를 이길 수 있으면 arr[A][C] = True
    4. 모든 선수에 대해서 0 <= i < N이고 i != A일 때 not(arr[A][i] or arr[i][A])이면 순위가 모호하다.

    :param n: 선수의 수.
    :param results: 경기 결과. [A, B]는 A가 B를 이겼다는 것을 의미함.
    :return: 순위가 명확한 선수의 수.
    """
    to = n + 1
    ans = 0
    arr = [[False for _ in range(to)] for _ in range(to)]

    for [a, b] in results: arr[a][b] = True
    for k in range(1, to):
        for i in range(1, to):
            for j in range(1, to):
                if arr[i][k] and arr[k][j]:
                    arr[i][j] = True

    for i in range(1, to):
        for j in range(1, to):
            if i != j and not (arr[i][j] or arr[j][i]): break
        else:
            ans += 1

    return ans


def solution2(n, results):
    from collections import defaultdict
    ans = 0
    win = defaultdict(set)      # 선수 i가 승리한 선수리스트
    lose = defaultdict(set)     # 선수 i가 패배한 선수리스트

    for [a, b] in results:
        win[a].add(b)
        lose[b].add(a)

    for i in range(1, n + 1):  # 선수 i에 대해서
        for winner in lose[i]: win[winner].update(win[i])  # 선수 i가 패배한 선수 j의 j가 승리한 선수 리스트에 선수 i가 승리한 사람들을 더한다.
        for loser in win[i]: lose[loser].update(lose[i])   # 선수 i가 승리한 선수 j의 j가 패배한 선수 리스트에 선수 j가 패배한 사람들을 더한다.

    for i in range(1, n + 1):
        if len(win[i]) + len(lose[i]) == n - 1: ans += 1

    return ans
