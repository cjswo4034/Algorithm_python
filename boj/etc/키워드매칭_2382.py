from collections import defaultdict

import sys

input = sys.stdin.readline
print = lambda x:sys.stdout.write(x)

class Page:
    def __init__(self, idx, arr):
        self.idx = f'P{idx}'
        self.arr = arr
        self.keywords = defaultdict(int)

    def set_keywords(self, N):
        cost = N
        for i in range(1, len(self.arr)):
            self.keywords[self.arr[i].lower()] = cost
            cost -= 1

    def query(self, query):
        return sum([(self.keywords[key] * query.keywords[key]) for key in query.keywords])

class Query:
    def __init__(self, idx, arr):
        self.idx = idx
        self.arr = arr
        self.keywords = defaultdict(int)
        self.related_pages = []

    def set_keywords(self, N):
        cost = N
        for i in range(1, len(self.arr)):
            self.keywords[self.arr[i].lower()] = cost
            cost -= 1

    def add_page_score(self, page, score):
        self.related_pages.append([score, page.idx])

    def get_related_pages(self):
        sorted_pages = sorted(self.related_pages, key=lambda p: (-p[0], int(p[1][1:])))[:5]
        res = f'Q{self.idx}: {" ".join([p[1] for p in sorted_pages])}\n'
        return res

keywords = set()
pages, queries = [], []
while True:
    inputs = input().split()
    if inputs[0] == 'E': break
    elif inputs[0] == 'P' : pages.append(Page(len(pages) + 1, inputs))
    else: queries.append(Query(len(queries) + 1, inputs))
    for i in range(1, len(inputs)): keywords.add(inputs[i].lower())

N = len(keywords)
for page in pages: page.set_keywords(N)
for query in queries:
    query.set_keywords(N)
    for page in pages:
        score = page.query(query)
        if score: query.add_page_score(page, score)
    print(query.get_related_pages())