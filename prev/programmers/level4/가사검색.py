class Trie:
    def __init__(self):
        self.children = dict()
        self.count = 0


def solution(words, queries):
    answer = []
    root, reversed_root = dict(), dict()
    for word in words:
        l = len(word)
        if l not in root:
            root[l] = Trie()
            reversed_root[l] = Trie()
        save(root[l], word)
        save(reversed_root[l], word[::-1])

    for query in queries:
        if len(query) not in root:
            answer.append(0)
        elif query[0] == '?':
            answer.append(find(reversed_root[len(query)], query[::-1]))
        else:
            answer.append(find(root[len(query)], query))
    return answer


def save(root, word):
    runner, children = root, None
    for ch in word:
        children = runner.children
        if ch not in children:
            children[ch] = Trie()
        runner.count += 1
        runner = children[ch]
    runner.count += 1


def find(root, query):
    runner = root
    for ch in query:
        if ch == '?':   # 참조할 수 없는 값이 들어왔을 때
            return runner.count
        if ch not in runner.children: return 0
        runner = runner.children[ch]
    return runner.count


print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]))