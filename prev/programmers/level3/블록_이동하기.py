def solution(board):
    visit = [[[] for _ in range(len(board[0]))] for _ in range(len(board))]
    drone = Drone(0, 0, 0, 1, True, 0)

    return bfs(board, visit, drone)


def bfs(map, visit, start):
    q = [start]
    visit[start.x1][start.y1].append([start.x2, start.y2])
    visit[start.x2][start.y2].append([start.x1, start.y1])
    direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    while q:
        curr = q.pop(0)
        candidates = get_candidates(curr, direction)
        for candidate in candidates:
            if not is_movable(map, visit, candidate, curr): continue

            if (candidate.x1 == len(map) - 1 and candidate.y1 == len(map) - 1) or \
                    (candidate.x2 == len(map) -1 and candidate.y2 == len(map) - 1): return candidate.cnt

            visit[candidate.x1][candidate.y1].append([candidate.x2, candidate.y2])
            visit[candidate.x2][candidate.y2].append([candidate.x1, candidate.y1])
            q.append(candidate)


def is_movable(map, visit, curr, prev):
    if is_out_of_range(map, curr): return False
    if map[curr.x1][curr.y1] or map[curr.x2][curr.y2]: return False
    if is_visited(visit, curr): return False
    if curr.horizontal != prev.horizontal and not rotatable(map, curr, prev): return False
    return True


def is_out_of_range(map, drone):
    if drone.x1 < 0 or drone.x2 < 0 or drone.y1 < 0 or drone.y2 < 0: return True
    if drone.x1 >= len(map) or drone.x2 >= len(map) or drone.y1 >= len(map) or drone.y2 >= len(map): return True
    return False


def is_visited(visit, drone):
    return [drone.x2, drone.y2] in visit[drone.x1][drone.y1] or \
           [drone.x1, drone.y1] in visit[drone.x2][drone.y2]


def rotatable(map, curr, prev):
    x1, y1 = min(curr.x1, prev.x1, curr.x2, prev.x2), min(curr.y1, prev.y1, curr.y2, prev.y2)
    x2, y2 = max(curr.x1, prev.x1, curr.x2, prev.x2), max(curr.y1, prev.y1, curr.y2, prev.y2)
    if map[x1][y1] or map[x1][y2] or map[x2][y1] or map[x2][y2]: return False
    return True


def get_candidates(drone, direction):
    res = []
    for d in direction:
        res.append(Drone(drone.x1 + d[0], drone.y1 + d[1],
                         drone.x2 + d[0], drone.y2 + d[1], drone.horizontal, drone.cnt + 1))
    # for i in range(2):
    #     res.append(Drone(drone.x1, drone.y1,
    #                      drone.x1 + (direction[i][0] if drone.horizontal else 0),
    #                      drone.y1 + (direction[i][0] if not drone.horizontal else 0),
    #                      not drone.horizontal, drone.cnt + 1))
    #     res.append(Drone(drone.x2 + (direction[i][0] if drone.horizontal else 0),
    #                      drone.y2 + (direction[i][0] if not drone.horizontal else 0),
    #                      drone.x2, drone.y2,
    #                      not drone.horizontal, drone.cnt + 1))
    if drone.horizontal:
        for i in range(2):
            res.append(Drone(drone.x1, drone.y1,
                             drone.x1 + direction[i][0], drone.y1, False, drone.cnt + 1))
            res.append(Drone(drone.x2 + direction[i][0], drone.y2,
                             drone.x2, drone.y2, False, drone.cnt + 1))
    else:
        for i in range(2, 4):
            res.append(Drone(drone.x1, drone.y1,
                             drone.x1, drone.y1 + direction[i][1], True, drone.cnt + 1))
            res.append(Drone(drone.x2, drone.y2 + direction[i][1],
                             drone.x2, drone.y2, True, drone.cnt + 1))
    return res


class Drone:
    def __init__(self, x1, y1, x2, y2, horizontal, cnt):
        self.x1, self.y1 = x1, y1
        self.x2, self.y2 = x2, y2
        self.horizontal = horizontal
        self.cnt = cnt

    def __repr__(self):
        return f'({self.x1}, {self.y1}), ({self.x2}, {self.y2}) {self.horizontal} -> {self.cnt}'


print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]))