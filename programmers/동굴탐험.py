from collections import defaultdict

def solution(n, path, order):
    al = defaultdict(list)
    visit = [False] * n
    after = [0] * n
    before = [0] * n
    
    for p in path:
        al[p[0]].append(p[1])
        al[p[1]].append(p[0])
    
    for o in order: before[o[1]] = o[0]
    
    if before[0] != 0: return False

    st = [el for el in al[0]]
    visit[0] = True

    while st:
        now = st.pop()

        if visit[now]: continue
        if not visit[before[now]]: 
            after[before[now]] = now
            continue

        visit[now] = True

        for el in al[now]: st.append(el)

        st.append(after[now])

    for v in visit:
        if not v: return False
    return True

print(solution(9, [[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]], [[8,5],[6,7],[4,1]]))