def solution(n, t, m, timetable):
    bus_stop = [540 + (i * t) for i in range(n)]
    timetable = sorted([time_2_int(time) for time in timetable])

    mem, i = [[] for _ in range(len(bus_stop))], 0    # i 번째 버스시간에 탈 수 있는 사람
    while timetable:
        curr_time = timetable.pop(0)
        while i < len(mem) and bus_stop[i] < curr_time: i += 1  # 지금 도착한 버스 시간보다 현재시간이 같거나 작아야됨
        if i < len(mem) and len(mem[i]) >= m: i += 1            # 현재 탈수 있는 정원보다 클 경우 다음 버스 타야됨
        if i == len(mem): break
        mem[i].append(curr_time)

    if len(mem[-1]) < m: return int_2_time(bus_stop[-1])
    return int_2_time(mem[-1][-1] - 1)


def int_2_time(integer):
    q, r = divmod(integer, 60)
    return str(q).rjust(2, "0") + ":" + str(r).rjust(2, "0")


def time_2_int(time):
    time = time.split(":")
    return int(time[0]) * 60 + int(time[1])


print(solution(1, 1, 5, ["08:00", "08:01", "08:02", "08:03"]))
print(solution(2, 10, 2, ["09:10", "09:09", "08:00"]))
print(solution(2, 1, 2, ["09:00", "09:00", "09:00", "09:00"]))
print(solution(1, 1, 5, ["00:01", "00:01", "00:01", "00:01", "00:01"]))
print(solution(1, 1, 1, ["23:59"]))
print(solution(10, 60, 45, ["23:59","23:59", "23:59", "23:59", "23:59", "18:00"]))
print(solution(10, 60, 10, ["17:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"] ))
