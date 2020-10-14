# 풍선이 살아남을 수 있는지 확인하는 방법
# -> 왼쪽 행렬에서 가장 작은 수와 오른쪽 행렬에서 가장 작은 수 둘 다 풍선보다 작다면 실패
# -> 하나만 작거나 둘 다 크다면 성공

# 행렬을 스캔하면서 해당 열에 큰 수 작은 수를 입력
# 왼->오, 오->왼 2번 스캔한다.
def solution(a):
    answer, length = 0, len(a)
    min_v = 1000000001
    left = [0 for _ in range(length)]
    # 1. 왼쪽에서 작은 수 찾기
    for i in range(length):
        left[i] = min_v
        if min_v > a[i]: min_v = a[i]

    min_v = 1000000001
    # 2. 오른쪽에서 작은 수 찾으면서 값 비교하기
    for i in range(length - 1, -1, -1):
        if a[i] < min_v or a[i] < left[i]: answer += 1
        if min_v > a[i]: min_v = a[i]

    return answer