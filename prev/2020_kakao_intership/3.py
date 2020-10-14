# 무식하게 - 정확도 1개 시간초과
def solution(gems):
    collect = len(set(gems))
    if collect == 1: return [1, 1]
    answer = [0, len(gems), len(gems)]
    for i in range(0, len(gems) - 1):
        for j in range(i + 1, len(gems)):
            if answer[2] < j - i: break
            if answer[1] - answer[0] > j - i and len(set(gems[i:j + 1])) == collect:
                answer = [i + 1, j + 1, j - i]
                if answer[2] == collect:
                    return answer[:2]
    return answer[:2]


# 앞과 앞이 같거나 뒤와 뒤가 같거나, 앞과 뒤가 같으면 아닐 때까지 앞을 제거
def solution2(gems):
    dict_gems = {gem:i for i, gem in enumerate(set(gems))}
    gems = [dict_gems[gem] for gem in gems]

    answer = [1, len(gems)]
    collect = (1 << len(dict_gems)) - 1

    bit_gems, l = 0, 0
    accumulate_gem = []
    for r, gem in enumerate(gems):
        bit_gems |=(1 << gem)
        accumulate_gem.append(gem)

        while len(accumulate_gem) > 1 and (accumulate_gem[l] in accumulate_gem[l + 1:]):
            l += 1

        if bit_gems == collect and answer[1] - answer[0] > r - l:    
            answer = [l + 1, r + 1]
    return answer


print(solution2(["DIA", "RUBY", "DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA", "RUBY"]))