class TrieNode:
    def __init__(self):
        self.child = {}
        self.count = {}
        self.terminate = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.reversed_root = TrieNode()

    def find(self, query):
        length, runner = len(query), None
        if query[0] == '?':
            runner = self.reversed_root
            query = query[::-1]
        else: runner = self.root

        for idx, q in enumerate(query):
            if q == '?': return runner.count[length - idx] if runner.count.get(length - idx) else 0
            if runner.terminate: return 0
            if not runner.child.get(q): return 0
            runner = runner.child[q]
        return 0
    
    def add(self, word, reversal = False):
        length, runner = len(word) - 1, None
        if reversal: runner = self.reversed_root
        else:
            runner = self.root
            self.add(word[::-1], True)

        if not runner.count.get(length + 1):
            runner.count[length + 1] = 0
        runner.count[length + 1] += 1

        for idx, w in enumerate(word):
            if not runner.child.get(w):
                runner.child[w] = TrieNode()
            runner = runner.child[w]

            if not runner.count.get(length - idx):
                runner.count[length - idx] = 0
            runner.count[length - idx] += 1
        runner.terminate = True

def solution(words, queries):
    answer = []
    trie = Trie()
    
    for word in words:
        trie.add(word)
    
    print(trie.root.child)
    print(trie.reversed_root.child)

    for query in queries:
        if query.count('?') == len(query):
            answer.append(trie.root.count[len(query)] if trie.root.count.get(len(query)) else 0)
            continue
        answer.append(trie.find(query))
        
    return answer


print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?", "?????"]))