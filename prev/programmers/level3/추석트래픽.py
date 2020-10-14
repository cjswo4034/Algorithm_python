from datetime import datetime
import re


def solution(lines):
    lines = [parse_str(line) for line in lines]
    lines.sort(key=lambda x:x[1])

    ans = 0
    for i in range(len(lines)):
        ans = max(ans, get_count(lines, i))

    return max([get_count(lines, i) for i in range(len(lines))])


def parse_str(line):
    criteria = line.rfind(" ")
    end = int(datetime.strptime(line[:criteria], "%Y-%m-%d %H:%M:%S.%f").timestamp() * 1000)
    start = re.sub("[^0-9]", "", line[criteria + 1:])
    start = int("{0:0<4}".format(start))
    start = end - start + 1

    return [start, end]


def get_count(lines, idx):
    count, criteria = 1, lines[idx][1] + 1000
    for el in lines[idx + 1:]:
        if el[0] < criteria:
            count += 1
    return count


# print(solution([
#     "2016-09-15 01:00:04.001 2.0s",
#     "2016-09-15 01:00:07.000 2s"]))
# print(solution([
#     "2016-09-15 01:00:04.002 2.0s",
#     "2016-09-15 01:00:07.000 2s"]))
print(solution([
    "2016-09-15 20:59:57.421 0.351s",
    "2016-09-15 20:59:58.233 1.181s",
    "2016-09-15 20:59:58.299 0.8s",
    "2016-09-15 20:59:58.688 1.041s",
    "2016-09-15 20:59:59.591 1.412s",
    "2016-09-15 21:00:00.464 1.466s",
    "2016-09-15 21:00:00.741 1.581s",
    "2016-09-15 21:00:00.748 2.31s",
    "2016-09-15 21:00:00.966 0.381s",
    "2016-09-15 21:00:02.066 2.62s"]))
