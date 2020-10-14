import sys
sys.setrecursionlimit(100000)

def solution1(k, room_number):
    mem = {}
    return [assign_room(mem, room) for room in room_number]

# recursive
def assign_room(mem, n):
    if n not in mem:
        mem[n] = n + 1 
        return n
    else: 
        mem[n] = assign_room(mem, mem[n])
        return mem[n]

# interactive
def solution2(k, room_number):
    answer, mem = [], {}
    for room in room_number:
        next_room = room
        visited = [next_room]
        while next_room in mem:
            next_room = mem[next_room]
            visited.append(next_room)

        for v in visited:
            mem[v] = next_room + 1

        answer.append(next_room)
    return answer

print(solution2(10, [1, 3, 4, 1, 3, 1]))

# 배정받으려는 방이 배정이 안됐을 경우
# 1) 해당 방을 배정한다.
# 2) 배정받은 방보다 크면서 배정이 안된 방을 가리킨다.

# 배정받으려는 방이 배정이 됐을 경우
# 1) 해당 방이 가리키는 다음 방을 배정한다.
# 2) 배정받은 방보다 크면서 배정이 안된 방을 가리킨다.

# k: 1 ~ 10^12 까지임. 어디에 저장?
# 배열: arr[k] -> 불가능
# 사전: dict[k] -> 가능