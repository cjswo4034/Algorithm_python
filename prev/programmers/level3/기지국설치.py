from math import ceil


def solution(n, stations, w):
    answer = 0
    location, width = (1, 2 * w + 1)
    for i in range(len(stations)):
        station = get_range(stations[i], w)
        if station[0] <= location <= station[1]:
            location = station[1] + 1
        else:
            answer += ceil((station[0] - location) / width)
            location = station[1] + 1
    if location <= n:
        answer += ceil((n - stations[-1] - w) / width)
    return answer


def get_range(station, w):
    return [station - w, station + w]


print(solution(11, [4, 11], 1))
print(solution(16, [9], 2))
