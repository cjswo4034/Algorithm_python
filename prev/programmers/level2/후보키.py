def solution(relation):
    visit, candidates = [], []
    for i in range(1, 1 << len(relation[0])):
        if visited(candidates, i): continue
        print(i)
        s = set()
        for r in relation: s.add(get_key(r, i))
        if len(s) == len(relation): candidates.append(i)
    print(candidates)
    return len(candidates)


def visited(visit, idx):
    for i in visit:
        if (i & idx) == i: return True
    return False


def get_key(rows, idx):
    res = []
    for i in range(len(rows)):
        if (idx & 1) == 1: res.append(rows[i])
        idx >>= 1
    return ''.join(res)


input = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
input = [
    ["1", "2", "3"],
    ["2", "2", "4"],
    ["3", "3", "5"],
    ["4", "3", "6"]
]
print(solution(input))
