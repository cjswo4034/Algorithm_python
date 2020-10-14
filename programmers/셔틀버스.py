class Bus:
    def __init__(self, maximum, arrived_time):
        self.maximum = maximum
        self.arrived_time = arrived_time
        self.passengers = []

    def pick_up(self, arrived_time):
        if len(self.passengers) == self.maximum: return False
        if arrived_time > self.arrived_time: return False

        self.passengers.append(arrived_time)
        return True

def solution(n, t, m, timetable):
    arrived_time = 9 * 60
    timetable = [str_to_time(tt) for tt in timetable]
    timetable.sort()
    
    buses = [Bus(m, arrived_time + (i * t)) for i in range(n)]
    
    for bus in buses:
        while timetable and bus.pick_up(timetable[0]):
            timetable.pop(0)
    
    if len(buses[-1].passengers) < m: return time_to_str(buses[-1].arrived_time)
    return time_to_str(buses[-1].passengers[-1] - 1)

def str_to_time(s):
    return int(s[:2]) * 60 + int(s[3:])

def time_to_str(time):
    return '%02d:%02d' % (time // 60, time % 60)

# 버스를 만든다.
# 버스를 순회하며 승객을 태운다.
# 마지막 버스에 대해서
# 자리가 남으면) 해당 버스의 도착시간
# 자리가 없으면) 해당 버스의 마지막 탑승객의 도착시간 -1분
print(solution(1, 1, 5, ["08:00", "08:01", "08:02", "08:03"]))