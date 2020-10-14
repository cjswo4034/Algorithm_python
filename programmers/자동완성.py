def solution(words):
    class Trie:
        def __init__(self):
            self.child = {}
            self.has_others = False
            self.terminate = False

    root, answer = Trie(), 0

    for word in words:  # Make Trie
        runner = root
        for w in word:
            if w in runner.child:
                runner.child[w].has_others = True
            else: runner.child[w] = Trie()
            runner = runner.child[w]
        runner.terminate = True

    for word in words:  # Query word
        runner = root
        for i, w in enumerate(word):
            runner = runner.child[w]
            if not runner.has_others:
                answer += i + 1
                break
        else: answer += len(word)

    return answer

def solution2(words):
    words.sort()
    ans = same_length(words[0], words[1])
    for i in range(1, len(words) - 1):
        l = same_length(words[i], words[i - 1])
        r = same_length(words[i], words[i + 1])
        ans += max(l, r)
    ans += same_length(words[-1], words[-2])
    return ans

# w1: 검사 주체, w2: 비교 대상
def same_length(w1, w2):
    length = min(len(w1), len(w2))
    for i in range(length):
        if w1[i] is not w2[i]: return i + 1
    return length + (0 if length == len(w1) else 1)

print(solution2(["word","war","warrior","wwrld"]))