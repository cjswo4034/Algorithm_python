from . import command


# A층에 있는 엘리베이터가 B층에 있는 사람을 태웠을 때. [도착지: C]
# 엘베 안에 B나 C층에 내리거나 타는 사람이 없을 때) 
#  -> 비용: C - B + 8 + (A - B + 엘베가 이동할 때 까지 시간)
# 엘베 안에 B층에 내리려는 사람이 있을 때
#  -> 비용: C - B + 4
# 엘베 안에 C층에 내리려는 사람이 있을 때
#  -> 비용: C - B + 4
# 엘베 안에 B층과 C층에서 내리려는 사람이 있을 때
#  -> 비용: C - B

# 특정 방향으로 가는 사람들 중에서 가장 작은 비용이 드는 사람
# 우선순위
# 1) 엘베 안에 있는 사람이 내리려는 층에 있으면서 내리는 층이 엘베 안에 있는 사람이 내리는 층일 경우
# 2) 엘베 안에 있는 사람이 내리려는 층에 있는 경우 (방향 같아야됨)
# 2) 엘베 안에 있는 사람이 내리려는 층에 내리려는 경우
# 3) 가는 방향이 같은 경우
# 

class Elevator:
    def __init__(self, res_elevator):
        self.id = res_elevator['id']
        self.floor = res_elevator['floor']
        self.status = res_elevator['status']
        self.passengers = [list(p.values()) for p in res_elevator['passengers']]

    def __repr__(self):
        return f'[{self.id}, {self.floor}층] ({self.status}) : {self.passengers}'

    # 현재 층에서 내릴 사람이 있거나 태울 사람이 있으면 True
    def is_call(self, calls):
        if self.floor in [e[3] for e in self.passengers]: return True
        if self.floor in [e[2] for e in calls]: return True
        return False

    # 현재 층에서 내릴 사람, 태울 사람의 id
    def get_passengers_to_do(self, calls):
        a = [passenger[0] for passenger in self.passengers if self.floor == passenger[3]]
        b = [call[0] for call in calls if self.floor == call[2]] [:8-len(self.passengers)]
        return a, b

    # 내릴 사람이 있는 경우 -> 승객이 가려는 방향으로
    # 내릴 사람이 없는 경우
    # 전 층에 사람이 없는 경우 -> stop
    # 현재 층을 기준으로 위에 있으면서 위로 가는 사람이 많다면 up, 아니면 down
    # 둘 다 0이면 -> 현재 층을 기준으로 위에 있는 사람이 많으면 up, 아니면 down
    def get_direction(self, call):
        if not self.passengers:
            if not call.calls: return "STOP"
            comp = call.upcalls_more_than_downcalls_by_floor(self.floor)
            if not comp:
                comp = call.upcalls_more_than_downcalls(self.floor)
                if not comp: return "STOP"
                return "UP" if comp == 1 else "DOWN"
            return "UP" if comp == 1 else "DOWN"
        return "UP" if self.floor < self.passengers[0][3] else "DOWN"

    # cmd 반환
    # TODO List
    # ENTER할 call들 선별하기. (방향확인)
    def action(self, call):
        res = command.Command(self.id)
        current_call = call.get_calls_by_floor(self.floor)
        calls_to_get_off, calls_to_take = self.get_passengers_to_do(current_call)

        if self.status == "UPWARD" or self.status == "DOWNWARD":
            if self.is_call(current_call): 
                if calls_to_take: call.remove_calls(calls_to_take)
                res.set_cmd("STOP")
            else:
                dir = self.get_direction(call)
                if dir == "UP": res.set_cmd(dir if self.status == "UPWARD" else "STOP")
                else: res.set_cmd(dir if self.status == "DOWNWARD" else "STOP")

        if self.status == "STOPPED":
            if not call.calls and not self.passengers: res.set_cmd("STOP")
            if self.is_call(current_call): 
                if calls_to_take: call.remove_calls(calls_to_take)
                res.set_cmd("OPEN")
            else: res.set_cmd(self.get_direction(call))

        if self.status == "OPENED":
            if self.is_call(current_call):
                if calls_to_get_off: res.set_cmd("EXIT", calls_to_get_off)
                elif calls_to_take:
                    call.remove_calls(calls_to_take)
                    res.set_cmd("ENTER", calls_to_take)
                else: res.set_cmd("CLOSE")
            else: res.set_cmd("CLOSE")
    
        return res
        """ 
        # upward & downward
        - up & down
            - 1. 현재 층에서 내리거나 태울 사람이 없을 때
        - stop
            - 1. 현재 층에서 내리거나 태울 사람이 있을 때
            - 2. 내릴 사람도 없고 모든 층에서 탈 사람도 없을 때

        # stopped
        - up & down
            - 1. 현재 층에서 내리거나 태울 사람이 없을 때 -> 탑승객들 방향 확인
        - open
            - 1. 현재 층에서 내리거나 태울 사람이 있을 때
        - stop
            - 1. 현재 층에서 내릴 사람과 모든 층에서 태울 사람이 없을 때

        # opened
        - open
            - 1. 현재 층에서 내리거나 태울 사람이 있을 때
        - enter & exit
            - 1. 현재 층에서 내리거나 태울 사람이 있을 때
        - close
            - 1. 현재 층에서 내리거나 태울 사람이 없을 때
        """