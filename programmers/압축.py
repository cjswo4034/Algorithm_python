def solution(msg):
    answer, j = [], 0
    d = {chr(i): i - 64 for i in range(65, 91)}
    for i in range(len(msg)):
        if i < j: continue
        j = i
        while j + 1 <= len(msg) and msg[i:j + 1] in d: j += 1
        answer.append(d[msg[i:j]])
        if j + 1 <= len(msg): d[msg[i:j + 1]] = len(d) + 1
    return answer

solution('TOBEORNOTTOBEORTOBEORNOT')