def dfs(r, c, count):
    global result
    if count >= result: return
    if c == 10:
        dfs(r + 1, 0, count)
        return
    
    if r == 10:
        result = min(result, count)
        return

    if arr[r][c] == 0:
        dfs(r, c + 1, count)
        return

    for color in range(5, 0, -1):
        if colors[color] == 0: continue
        if fillable(r, c, color) == False: continue

        fill(r, c, color, 0)
        colors[color] -= 1
        
        dfs(r, c + color, count + 1)

        fill(r, c, color, 1)
        colors[color] += 1

def fillable(r, c, size):
    if r + size > 10 or c + size > 10: return False
    
    for i in range(size):
        for j in range(size):
            if arr[r + i][c + j] == 0: return False
    return True

def fill(r, c, size, value):
    for i in range(size):
        for j in range(size):
            arr[r + i][c + j] = value 

result = 987654321
arr = [[int(el) for el in input().split()] for _ in range(10)]
colors = [0, 5, 5, 5, 5, 5]

dfs(0, 0, 0)
print(result if result != 987654321 else -1)