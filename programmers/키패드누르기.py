def solution(numbers, hand):
    answer = ''
    l, r = [1, 3], [1, 3]
    for num in numbers:
        if num == 0: num = 11
        idx = num // 3
        if num % 3 == 1:
            answer += 'L'
            l = [1, idx]
        elif num % 3 == 0:
            answer += 'R'
            r = [1, idx - 1]
        else:
            if next_hand(l, r, idx, hand) == 'right':
                answer += 'R'
                r = [0, idx]
            else:
                answer += 'L'
                l = [0, idx]
    return answer

def next_hand(l, r, idx, hand):
    rd = r[0] + abs(r[1] - idx)
    ld = l[0] + abs(l[1] - idx)

    if rd < ld: return 'right'
    elif rd > ld: return 'left'
    else: return hand

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))