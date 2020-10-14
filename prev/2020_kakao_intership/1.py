def solution(numbers, hand):
    answer = ''
    l, r = [3, 0], [3, 0]   # 0 본래 위치, 1: 중앙
    left = [1, 4, 7]
    right = [3, 6, 9]
    others = [2, 5, 8, 0]
    for i, number in enumerate(numbers):
        if number in left:
            l = [left.index(number), 0]
            answer += 'L'
        elif number in right:
            r = [right.index(number), 0]
            answer += 'R'
        else:
            l_pos = abs(l - others.index(number))
            if l[1]: l_pos -= 1
            r_pos = abs(r - others.index(number))
            if r[1]: r_pos -= 1
            if l_pos < r_pos:
                l = [others.index(number), 1]
                answer += 'L'
            elif l_pos > r_pos:
                r = [others.index(number), 1]
                answer += 'R'
            else:
                if hand == "left":
                    l = [others.index(number), 1]
                    answer += 'L'
                else:
                    r = [others.index(number), 1]
                    answer += 'R'
        print(number, l, r)
    return answer


print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))