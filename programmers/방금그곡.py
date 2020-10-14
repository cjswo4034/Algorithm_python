import re

def solution(m, musicinfos):
    m = trans_musicinfo(m, len(m))
    candidate = [0, '(None)']
    # musicinfos의 원소 musicinfo에 대해서
    for musicinfo in musicinfos:
        start, end, title, info = musicinfo.split(',')

        # 1. 재생 시간을 구한다. ([1] - [0])
        playtime = str_to_time(end) - str_to_time(start)
        
        # 2. 악보의 #을 소문자로 변경
        info = trans_musicinfo(info, playtime)

        # 3. 악보를 재생시간만큼 늘림
        info = info * (playtime // len(info)) + info[:playtime % len(info)]
        
        # 4. m과 일치하는지 비교
        if info.count(m) and candidate[0] < playtime: candidate = [playtime, title]
    
    return candidate[1]

def trans_musicinfo(info, playtime):
    return ''.join([i if len(i) == 1 else i[0].lower() for i in re.findall('[A-Z][#]?', info)])

def str_to_time(s):
    return int(s[:2]) * 60 + int(s[3:])

print(solution("CDEFGAC", ["12:00,12:06,HELLO,CDEFGA"]))