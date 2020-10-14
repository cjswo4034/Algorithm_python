# 1. words를 순회하면서 dictionary를 생성
# 2. word를 하나씩 변환하면서 dictionary에 추가
# 3. query를 dict에서 검색 후 반환


def solution(words, queries):
    dictionary = create_dict(words)
    answer = [dictionary[query] if dictionary.get(query) else 0 for query in queries]
    return answer


def create_dict(words):
    ans = dict()
    for word in words:
        for i in range(1, len(word)):
            pre = '?' * (i) + word[i:]
            post = word[:i] + '?' * (len(word) - i)
            if ans.get(pre): ans[pre] += 1
            else: ans[pre] = 1
            if ans.get(post): ans[post] += 1
            else: ans[post] = 1
    return ans


print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"],
               ["fro??", "????o", "fr???", "fro???", "pro?"]))