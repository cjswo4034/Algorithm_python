class Trie:
    def __init__(self):
        self.children_map = dict()
        self.terminates = False
        self.count = 0
        self.depth = 0

    def insert(self, word, depth):
        if not word or len(word) == 0: return
        self.depth = depth

        child = self.children_map.get(word[0])
        if not child:
            child = Trie()
            self.children_map[word[0]] = child

        if len(word) > 1:
            child.insert(word[1:], depth + 1)
            child.terminates = False
        else:
            child.terminates = True
        child.count += 1

    def get_all_child(self):
        return list(self.children_map.values())

    def get_children(self, ch):
        if ch:
            return [self.children_map.get(ch)]
        else:
            return self.children_map.values()

    def is_terminated(self):
        return self.terminates

    def get_children_count(self, ch):
        return len(self.children_map)


def find(root, query):
    idx = 0
    q = [root]
    while q:
        length = len(q)
        while length > 0:
            curr = q.pop(0)
            next = curr.children_map.get(query[idx])
            if query[idx] == '?':
                q.extend(curr.get_all_child())
            elif next:
                q.append(next)
            else:
                return 0

            length -= 1

        idx += 1
        # print(len(q))
        if idx == len(query):
            return len(q)
    # print("end")
    return 0


def solution(words, queries):
    root = Trie()
    for word in words:
        root.insert(word, 1)

    for query in queries:
        print(query, find(root, query))

    #
    # ans = []
    # for i in range(1, len(words[0]) + 1):
    #     print(words[0][:i], find(root, words[0][:i]))


print(solution(
    ["frodo", "front", "frost", "frozen", "frame", "kakao"],
    ["f", "fr", "fro", "fro?", "fro??", "????o", "fr???", "fro???", "pro?"]))

# if ch != '?':
#     if next.children_map.get(ch):
#         q.append(next.children_map.get(ch))
#         ans = next.children_map.get(ch).count
#     else:
#         return 0
# else:
#     count = next.get_all_child()
#     while count > 0:
#         count -= 1
