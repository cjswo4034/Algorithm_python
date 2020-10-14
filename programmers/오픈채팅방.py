from collections import defaultdict

def solution(record):
    messages = {'Enter': '님이 들어왔습니다.', 'Leave': '님이 나갔습니다.'}
    cmds, db = [], defaultdict()
    for r in record:
        cmd = r.split(" ")
        if cmd[0] != 'Leave': db[cmd[1]] = cmd[2]
        if cmd[0] != 'Change': cmds.append(cmd)
    
    return [db[cmd[1]] + messages[cmd[0]] for cmd in cmds]

# Enter)
#  1. uid가 캐쉬에 있는지 확인한다.
#      O) 아이디를 변경한다.
#      X) Pass
# Leave)
#  1. 출력
# Change)
#  1. 해당 uid의 아이디 변경

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))