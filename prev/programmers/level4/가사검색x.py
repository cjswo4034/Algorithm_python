def solution(words, queries):
    dictionary = create_dict(words)
    for i in range(len(queries)):
        query = trans_qm_2_num(queries[i])
        if dictionary.get(query):
            queries[i] = dictionary[query]
        else:
            queries[i] = 0
    return queries


def trans_qm_2_num(query):
    qm_count = query.count('?')
    if query[0] == '?':
        query = str(qm_count) + query[qm_count:]
    else:
        query = query[:-qm_count] + str(qm_count)
    return query


def create_dict(words):
    ans = dict()
    for word in words:
        for i in range(1, len(word)):
            pre = str(i) + word[i:]
            post = word[:i] + str(len(word) - i)
            if ans.get(pre): ans[pre] += 1
            else: ans[pre] = 1
            if ans.get(post): ans[post] += 1
            else: ans[post] = 1
    return ans


print(solution(['abcde'], ['?????']))