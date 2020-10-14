from datetime import datetime
import time 

class Log:
    def __init__(self, start, to):
        self.start = start
        self.to = to

def solution(lines):
    answer = 0
    logs = [parser(line) for line in lines]
    logs = sorted(logs, key=lambda x: (x.to, x.start))
    
    for i in range(0, len(logs)):
        tmp = sum(map(lambda log: 1 if logs[i].to > log.start - 1000 else 0, logs[i:]))
        answer = max(answer, tmp)

    return answer

def parser(line):
    sec = line[0:line.rindex(" ")]
    duration = float(line[line.rindex(" "): -1]) * 1000

    end = int(datetime.strptime(sec, '%Y-%m-%d %H:%M:%S.%f').timestamp() * 1000)
    start = end - int(duration) + 1
    return Log(start, end)


solution(["2016-09-15 01:00:04.001 2.0s"])