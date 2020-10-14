def solution(records):
    answer = []
    users = dict()
    convert_cmd = {'Enter': '님이 들어왔습니다.', 'Leave': '님이 나갔습니다.'}
    for record in records:
        record = record.split(' ')
        if len(record) == 3:
            users[record[1]] = record[2]

    for record in records:
        record = record.split(' ')
        if record[0] != 'Change':
            answer.append(users[record[1]] + convert_cmd[record[0]])

    return answer


li = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(li))
