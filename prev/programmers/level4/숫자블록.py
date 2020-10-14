def solution(begin, end):  # TODO 문제 개편됨.
    # 문제 조건이 잘못됨 (1천만 까지의 블록을 사용할 수 있으나 실제론 5억이 통과됨)
    # 원래 풀이
    # 1) 1부터 end 까지 순회
    # 2) prime 으로 나누어 떨어지고 1천만 이하이면 append
    # 3) 그 외에는 pass
    answer = []
    if begin == 1:
        answer.append(0)
        begin += 1
    for i in range(begin, end + 1):
        if i % 2 == 0:
            answer.append(i // 2)
        else:
            flag = len(answer)
            for j in range(3, i):
                if j * j > i:
                    break
                if i % j == 0:
                    answer.append(i // j)
                    break
            if flag == len(answer):
                answer.append(1)
    return answer


print(solution(1, 10))