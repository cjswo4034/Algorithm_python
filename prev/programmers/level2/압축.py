def solution(msg):
    dictionary = {chr(i): i - 64 for i in range(ord('A'), ord('Z') + 1)}
    answer = []

    msg, curr = list(msg[1:]), msg[0]
    while curr:
        while msg and dictionary.get(curr):
            curr += msg.pop(0)

        if dictionary.get(curr):
            answer.append(dictionary[curr])
            break

        answer.append(dictionary[curr[:-1]])
        dictionary[curr] = len(dictionary) + 1
        curr = curr[-1]

    return answer


print(solution('TOBEORNOTTOBEORTOBEORNOT'))
print(solution('KAKAO'))
