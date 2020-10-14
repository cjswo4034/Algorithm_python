def solution(begin, target, words):
    q = [[begin, 0]]
    visited = [False for _ in range(len(words))]

    ans = 0
    while q:
        curr = q.pop(0)
        print(curr)
        if curr[0] == target:
            ans = curr[1]
            break

        for i in range(len(words)):
            if not visited[i] and isNext(curr[0], words[i]):
                visited[i] = True
                q.append([words[i], curr[1] + 1])

    return ans


def isNext(str1, str2):
    cnt = 0
    for i in range(len(str1)):
        if str1[i] is not str2[i]:
            cnt += 1

    return True if cnt == 1 else False


print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))