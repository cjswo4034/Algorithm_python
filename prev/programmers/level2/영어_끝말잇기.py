def solution(n, words):
    answer = [0, 0]

    turn = 1
    mem, prev = [words[0]], words[0]
    for idx, word in enumerate(words[1:]):
        if prev[-1] == word[0] and mem.count(word) == 0:
            prev = word
            mem.append(word)
        else:
            p_idx = n if (idx + 2) % n == 0 else (idx + 2) % n
            answer = [p_idx, turn]
            break
        if (idx + 2) % n == 0:
            turn += 1

    for turn in range(1, len(words)):
        if words[turn - 1][-1] != words[turn][0] or\
            words[turn] in words[:turn]:
            return [(turn % n) + 1, (turn // n) + 1]

    # for p in range(1, len(words)):
    #     if words[p][0] != words[p - 1][-1] or words[p] in words[:p]: return [(p % n) + 1, (p // n) + 1]
    # else:
    #     return [0, 0]

    return answer


print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
print(solution(5,	["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))
print(solution(2,	["hello", "one", "even", "never", "now", "world", "draw"]))