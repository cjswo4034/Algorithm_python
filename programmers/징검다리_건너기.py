def solution(stones, k):
    if k == 1: return min(stones)

    l, r, answer = 1, 200000000, 0
    while l <= r:
        m, max_seq, seq = (l + r) >> 1, 0, 0
        for stone in stones:
            if stone < m: seq += 1
            else:
                max_seq = max(max_seq, seq)
                seq = 0
        
        max_seq = max(max_seq, seq)
        
        if max_seq >= k: r = m - 1
        else:
            answer = max(answer, m) 
            l = m + 1

    return answer

print(solution([2, 2, 5, 3, 2, 1, 4, 2, 2, 3], 3))