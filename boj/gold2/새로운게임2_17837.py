import sys

input = sys.stdin.readline

'''
종료조건: 4개 이상쌓일 때
         반복될 때 -> 1001 이상이면 종료
하얀색
1. 현재 위치에서 자기 위에 있는 말을 지운다.
2. 다음 위치를 정한다.
3. 다음 위치로 자기 위에 있는 말을 옮긴다.

빨간색 (순서변경)
1. 현재 위치에서 자기 위에 있는 말을 지운다.
2. 다음 위치를 정한다.
3. 다음 위치로 자기 위에 있는 말을 옮긴다.
4. 다음 위치에 있는 말들의 순서를 변경한다. *

파란색
1. 현재 위치에서 자기 위에 있는 말을 지운다.
2. 방향을 바꾼다. *
3. 바뀐 방향으로 다음 위치를 정한다.
4. 다음 위치의 발판을 확인한다. *
    a. 다음 위치가 파란색 발판이거나 맵의 끝인 경우 현재 위치에 있는다.
    b. 다음 위치가 하얀색이면 이동한다.
    c. 다음 위치가 빨간색이면 순서를 변경한다.
5. 다음 위치로 자기 위에 있는 말을 옮긴다.

공통 (현재 위치, 현재 위치에서의 인덱스, 다음 위치[방향], 다음 위치에서 인덱스)
1. 현재 위치에서 자기 위에 있는 말을 지운다.
2. 다음 위치를 정한다.
3. 다음 위치로 자기 위에 있는 말을 옮긴다.
'''

class Horse:
    def __init__(self, *args):
        self.pos = [args[0] - 1, args[1] - 1]
        self.dir = args[2] - 1

    def action(self, arr, mem):
        pos = self.get_next()
        if not self.validation(pos): cmd = 2
        else: cmd = arr[pos[0]][pos[1]]
        
        horses = self.remove_all(mem, self.pos)
        if cmd == 2:
            self.change_dir()
            pos = self.get_next()
            
            if not self.validation(pos) or arr[pos[0]][pos[1]] == 2:
                return self.move(mem, self.pos, horses)

            cmd = arr[pos[0]][pos[1]]
        if cmd != 2:
            return self.move(mem, pos, horses if cmd == 0 else horses[::-1])

    def validation(self, pos):
        if pos[0] < 0 or pos[1] < 0 or pos[0] >= n or pos[1] >= n: return False
        return True

    def change_dir(self):
        if self.dir == 0: self.dir = 1
        elif self.dir == 1: self.dir = 0
        elif self.dir == 2: self.dir = 3
        else: self.dir = 2

    def move(self, mem, pos, horses):
        mem[pos[0]][pos[1]] += horses
        for h in horses: h.pos = pos[:]
        return len(mem[pos[0]][pos[1]])

    def get_next(self):
        return self.pos[0] + d[self.dir][0], self.pos[1] + d[self.dir][1]

    def remove_all(self, mem, pos):
        idx = mem[pos[0]][pos[1]].index(self)
        res = mem[pos[0]][pos[1]][idx:]
        mem[pos[0]][pos[1]] = mem[pos[0]][pos[1]][:idx]
        return res


d = [[0, 1], [0, -1], [-1, 0], [1, 0]]
n, k = map(int, input().split())    # 크기, 말 개수
arr = [list(map(int, input().split())) for i in range(n)]
horses = [Horse(*map(int, input().split())) for i in range(k)]
mem = [[[] for _ in range(n)] for _ in range(n)]

for h in horses: mem[h.pos[0]][h.pos[1]].append(h)

ans = 0
for i in range(1000):
    for h in horses:
        if h.action(arr, mem) >= 4:
            ans = i + 1
            break
    if ans: break

if ans == 0: ans -=1
print(ans)