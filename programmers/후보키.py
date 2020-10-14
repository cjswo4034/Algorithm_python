def solution(relation):
    answer, candidates = 0, []
    backtracking(relation, 0, 0, candidates)
    candidates.sort(key=lambda x: bin(x).count('1'))
    
    check = [True] * len(candidates)

    for i in range(len(candidates)):
        if not check[i]: continue
        for j in range(i + 1, len(candidates)):
            if candidates[i] & candidates[j] == candidates[i]:
                check[j] = False
    return check.count(True)

def backtracking(relation, depth, col, candidates):
    if depth == len(relation[0]):
        if isCandidates(relation, col):
            candidates.append(col)
        return
    
    backtracking(relation, depth + 1, col | (1 << depth), candidates)
    backtracking(relation, depth + 1, col, candidates)

def isCandidates(relation, col):
    s = set()
    for r in relation:
        s.add(''.join([r[i] for i in range(len(relation[0])) if (1 << i) & col]))
    return len(s) == len(relation)

# 탐색 중인 후보키와 visit 원소들과 or 연산을 했을 때

# 상위 후보키(후보키를 구성하는 열의 개수가 적은 것) 중에서 OR 연산 결과가 연산에 사용된 상위 후보키면 X

# 자신 포함 or 비포함 했을 때 depth == n 이면 후보 검사
# 후보키를 구성하는 열의 개수 오름차순해서 제외시키기

print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))