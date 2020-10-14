def solution(user_id, banned_id):
    s = set()
    dfs(s, user_id, banned_id, 0, 0)
    return len(s)

def dfs(s, user_id, banned_id, visited, depth):
    if depth >= len(banned_id): 
        s.add(visited)
        return

    for idx, uid in enumerate(user_id):
        if visited & (1 << idx) or not match(uid, banned_id[depth]): continue
        visited |= (1 << idx)
        dfs(s, user_id, banned_id, visited, depth + 1)
        visited ^= (1 << idx)

def match(uid, bid):
    if len(uid) != len(bid): return False
    for u, b in zip(uid, bid):
        if b == '*' or u == b: continue
        return False
    return True

print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))
# print(solution(["frodo", "fradi", "crodo", "crod1", "crod2", "crod3", "crod4", "crod5"], ["*****", "*****", "*****", "*****", "*****", "*****", "*****", "*****" ]))
