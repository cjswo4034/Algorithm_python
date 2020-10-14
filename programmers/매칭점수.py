import re

class Page():
    def __init__(self, d):
        self.a = d['a']
        self.idx = d['idx']
        self.tot_point = d['body']
        self.add_point = (self.tot_point / len(self.a)) if self.a else 0

def solution(word, pages):
    pages = [parser(page, word.lower(), idx) for idx, page in enumerate(pages)]
    pages = {page[0]: Page(page[1]) for page in pages}
    for title in pages:
        for aa in pages[title].a:
            if aa in pages:
                pages[aa].tot_point += pages[title].add_point
    res = [[v.tot_point, v.idx] for v in pages.values()]
    return sorted(res, key=lambda r: (-r[0], r[1]))[0][1]

def parser(page, query, idx):
    html = {'idx': idx}
    page = page.replace('\n', ' ').replace('\t', ' ')
    title = re.search('<meta property=\\"og:url\\" content=\\"(https:\/\/[\S]*)\\\"', page).group(1)
    
    html['a'] = re.findall('(?<=\<a href=\\\")[^\\"]+', page)

    body = re.search('(?<=\<body\>).+(?=\<\/body\>)', page).group() # .lower().split(' ') 하고 밑에 줄 없애도 무방. 케이스 중 a=".+{query}.+" 있으면 틀림
    body = re.sub('<a[^\>]+"\>', '', body).replace("</a>", "").lower().split(' ')
    html['body'] = sum([re.findall('[a-z]+', b).count(query) for b in body if b])
    return title, html
    
print(solution('blind', ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]))
# url: meta 태크 property="og:url"의 url 속성값
# 외부링크: body 태그 내의 a 태그 url 값
# 검색어 body 태그 내에서 태그로 감싸지지 않은 값 

# 기본점수 : 해당 웹페이지의 텍스트 중, 검색어가 등장하는 횟수
# 외부링크 : 다른 외부 페이지로 연결된 링크의 개수
# 링크점수 : 해당 웹페이지로 링크가 걸린 다른 웹페이지의 (기본점수 ÷ 외부 링크 수)의 총합
# 매칭점수 : 기본점수와 링크점수의 합

# 검색어 word와 웹페이지의 HTML 목록인 pages가 주어졌을 때, 매칭점수가 가장 높은 웹페이지의 index (여러 개면 제일 작은 수)
