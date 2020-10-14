# 1. musicinfo를 초기화한다.
# 2. 초기화할 때 악보정보를 재생시간만큼 늘인다.
#    (math.ceil(재생시간 / 악보길이) * 악보)[:재생시간]
# 3. 모든 musicinfo에 대해서 정보가 m을 포함하면 answer에 포함한다.
# 4. 여러개일 경우 재생시간 -> 입력시간 순으로 반환한다.
import re


class MusicInfo():
    def __init__(self, music_info, idx, comp):
        music_info = music_info.split(',')

        self.idx = idx
        self.name = music_info[2]
        self.running_time = get_running_time(music_info[0], music_info[1])
        self.info = get_origin_info(comp, music_info[3], self.running_time)

    def is_contain(self, m):
        if self.info.count(m) == 0: return False
        i = self.info.index(m)
        while i < len(self.info):
            sharp_pos = i + len(m)
            if sharp_pos < len(self.info) and self.info[sharp_pos] == '#':
                if self.info.count(m, sharp_pos) == 0: return False
                i = self.info.index(m, sharp_pos)
            else: return True
        return False


def get_origin_info(comp, music_info, running_time):
    res = comp.findall(music_info)
    q, r = divmod(running_time, len(res))
    res = res * q + res[:r]
    return ''.join(res)


def get_running_time(start, end):
    start = start.split(':')
    end = end.split(':')
    return int(end[0]) * 60 + int(end[1]) - int(start[0]) * 60 - int(start[1])


def solution(m, music_infos):
    answer = []
    comp = re.compile('[\D][#]?')
    for i, music_info in enumerate(music_infos):
        music_info = MusicInfo(music_info, i, comp)
        if music_info.is_contain(m):
            answer.append(music_info)
    if answer:
        answer = sorted(answer, key=lambda mi: (-mi.running_time, mi.idx))
        return answer[0].name
    return '(None)'


# print(solution("ABCDEFG", ["12:01,12:16,HELLO,CDEFGAB", "12:00,12:14,HELLO2,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
# print(solution("ABC",	["12:00,12:14,HELLO,C#D#EFGAB", "13:00,13:12,WORLD,ABCDEF"]))
