def solution(k, room_number):
    return solution1(k, room_number)


# 무작정 풀기 (효율성 X)
def solution1(k, room_number):
    # k 길이의 boolean 배열을 만들어서 관리
    # room_number 를 순회한다.
    # 이미 방문했으면 그보다 크면서 False인 index를 찾는다.
    answer = []
    visited = set()
    for i in range(len(room_number)):
        j = room_number[i]
        while j < k and j in visited:
            j += 1
        visited.add(j)
        answer.append(j)
    return answer


def solution2(k, room_number):
    answer = []
    mem = dict()
    for room in room_number:
        answer.append(find(mem, room))
    return answer


# 이미 배정된 방일 경우 node의 parent를 배정한다.
def find(mem, room):
    if room not in mem:
        mem[room] = room + 1
        return room
    else:
        mem[room] = find(mem, mem[room])
        return mem[room]


print(solution2(10, [1,1, 1, 2, 1]))