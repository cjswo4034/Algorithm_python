""" [Gold 1]
1. 뱀의 머리가 위치한 좌표에 현재 머리의 방향으로 time 만큼 전진한다.
2. 전진 이전의 머리 위치부터 현재 머리 위치를 선분으로 저장한다.
3. 이전의 선분들에 대해서 계산한 2가 겹치지 않을 때까지 각각의 명령들을 1부터 수행한다.
** L: 반시계, R: 시계방향으로 회전
"""
import sys


input = sys.stdin.readline
l = int(input())
n = int(input())
DIR = ((1, 0), (0, -1), (-1, 0), (0, 1))  # R D L U
RANGE = (-l, l)


def is_inner(pos, value):
    return pos[0] <= value <= pos[1]


class Line:
    def __init__(self, s, e):
        self.s = tuple(s)
        self.e = tuple(e)

    def is_overlapped(self, line):
        l1s_x_same = self.s[0] == self.e[0]     # True: 세로, False: 가로
        l2s_x_same = line.s[0] == line.e[0]

        l1_x, l1_y = self.get_xy() if not l2s_x_same else line.get_xy()
        l2_x, l2_y = line.get_xy() if not l2s_x_same else self.get_xy()
        if l1s_x_same is not l2s_x_same:    # 교차할 때
            return is_inner(l1_y, l2_y[0]) and is_inner(l2_x, l1_x[0])
        elif l1s_x_same:                    # 둘 다 세로
            if l1_x[0] != l2_x[0]: return False
            if is_inner(l1_y, l2_y[0]) or is_inner(l1_y, l2_y[1]): return True
            if is_inner(l2_y, l1_y[0]) or is_inner(l2_y, l1_y[1]): return True
        else:                               # 둘 다 가로
            if l1_y[0] != l2_y[0]: return False
            if is_inner(l1_x, l2_x[0]) or is_inner(l1_x, l2_x[1]): return True
            if is_inner(l2_x, l1_x[0]) or is_inner(l2_x, l1_x[1]): return True
        return False

    def get_xy(self):
        x = (min(self.s[0], self.e[0]), max(self.s[0], self.e[0]))
        y = (min(self.s[1], self.e[1]), max(self.s[1], self.e[1]))
        return x, y


class Snake(object):
    def __init__(self):
        self.t = 0
        self.dir = 0
        self.head = [0, 0]
        self.bodies = []

    def move(self, t, next_dir):
        # 이번 이동 경로, 다음 머리 위치 (x, y)
        cur_body, (nx, ny) = self.process_before_move(t)

        # 이동했을 경우 몸통에 부딪히지 않고 이동할 수 있는가?
        res = self.is_not_overlapped(cur_body)

        # 이동한 머리가 범위를 벗어나는가?
        res = self.validate_range(res, nx, ny)

        # 무사히 이동했다면 파라미터 조정. 아니라면 생존시간 반환
        return self.process_after_move(res, t, next_dir, cur_body)

    def process_before_move(self, t):
        dx = DIR[self.dir][0] * t
        dy = DIR[self.dir][1] * t

        nx = self.head[0] + dx
        ny = self.head[1] + dy

        return Line(self.head, [nx, ny]), (nx, ny)

    def process_after_move(self, res, t, next_dir, cur_body):
        # 무사히 이동할 수 있다면
        # (1) 시간갱신, (2) 방향수정, (3) 머리 좌표 이동, (4) 이동 경로 추가
        if res[0]:
            self.t += t
            self.dir = (self.dir + 4 + next_dir) % 4
            self.head = cur_body.e
            self.bodies.append(cur_body)
        else: res[1] += self.t
        return res

    def validate_range(self, res, nx, ny):
        if not res[0]: return res
        if not (is_inner(RANGE, nx) and is_inner(RANGE, ny)):
            if RANGE[0] > nx: res[1] = self.head[0] - RANGE[0] + 1  # 왼쪽
            if RANGE[0] > ny: res[1] = self.head[1] - RANGE[0] + 1  # 아래쪽
            if RANGE[1] < nx: res[1] = RANGE[1] - self.head[0] + 1  # 오른쪽
            if RANGE[1] < ny: res[1] = RANGE[1] - self.head[1] + 1  # 위쪽
            res[0] = False
        return res

    # 이번에 이동하려는 경로 body가 기존의 이동 경로와 충돌하지 않는다면 False
    def is_not_overlapped(self, body):
        res = [True, 2 * 10 ** 12]

        x, y = body.s
        for i in range(len(self.bodies) - 2):
            (min_x, max_x), (min_y, max_y) = self.bodies[i].get_xy()
            if body.is_overlapped(self.bodies[i]):
                if self.dir == 0 and res[1] > min_x - x: res[1] = min_x - x  # 머리가 오른쪽으로 가니까 충돌한 선분들 중 작은 x값
                if self.dir == 1 and res[1] > y - max_y: res[1] = y - max_y  # 머리가 아래쪽으로 가니까 충돌한 선분들 중 큰 y값
                if self.dir == 2 and res[1] > x - max_x: res[1] = x - max_x  # 머리가 왼쪽으로 가니까 충돌한 선분들 중 큰 x값
                if self.dir == 3 and res[1] > min_y - y: res[1] = min_y - y  # 머리가 위쪽으로 가니까 충돌한 선분들 중 작은 y값
                res[0] = False
        return res


ans = [True, 0]
snake = Snake()
for _ in range(n):
    t, ch = input().split()
    t = int(t)
    cmd = -1 if ch == 'L' else 1

    ans = snake.move(t, cmd)
    if not ans[0]: break

# 명령 전부 수행했는데 살아있을 경우
if ans[0]: ans = snake.move(l * 2 + 1, 1)

print(ans[1])
