from html.parser import HTMLParser
import re

class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.body = False
        self.a = False
        self.url = ''
        self.contents = []
        self.external_links = []

    def handle_starttag(self, tag, attrs):
        if tag == 'meta':
            self.url = self.get_url(attrs)
        if tag == 'body':
            self.body = True
        if self.body and tag == 'a':
            self.a = True
            href = self.get_href(attrs)
            if len(href) > 0: self.external_links.extend(href)

    def handle_endtag(self, tag):
        if tag == 'body': self.body = False
        if tag == 'a': self.a = False

    def get_url(self, attrs):
        og_url = False
        for attr in attrs:
            if attr[0] == 'property': og_url = True
            if og_url and attr[0] == 'content': return attr[1]

    def handle_data(self, data):
        if self.body and data.strip() and not self.a: self.contents.append(data.strip())

    def get_href(self, attrs):
        return [attr[1] for attr in attrs if attr[0] == 'href']

    def get_data(self):
        res = [self.url, self.contents, self.external_links]
        self.__init__()
        return res


class WebPage():
    def __init__(self, index, url, contents, external_links):
        self.index = index
        self.url = url
        self.contents = contents
        self.external_links = external_links

        self.match_point = 0
        self.normal_point = 0
        self.external_point = 0

    def get_point(self, comp, word):
        self.normal_point = sum([get_point(comp, content, word) for content in self.contents])
        self.match_point += self.normal_point

    def adjust_match_point(self, point):
        self.match_point += point

    def __repr__(self):
        return f'{self.index}: {self.url}, {self.match_point}({self.normal_point}, {self.external_point})'


def get_point(comp, content, word):
    return comp.findall(content.lower()).count(word.lower())

def solution(word, pages):
    comp = re.compile('[a-zA-Z]+')
    html_parser = MyHTMLParser()
    web_dict = dict()
    for i, html in enumerate(pages):
        html_parser.feed(html)
        data = html_parser.get_data()  # url, contents, external_links
        web_page = WebPage(i, data[0], data[1], data[2])
        web_page.get_point(comp, word)
        web_dict[data[0]] = web_page

    for web in web_dict.values():
        for external_link in web.external_links:
            if web_dict.get(external_link):
                web_dict[external_link].adjust_match_point(web.normal_point / len(web.external_links))

    res = []
    for web in web_dict.values():
        res.append(web)

    res.sort(key=lambda x: (-x.match_point, x.index))
    return res[0]
