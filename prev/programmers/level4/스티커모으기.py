def solution(stickers):  # 통과, 공간점유가 많음
    if len(stickers) < 3: return max(stickers)
    mem1 = [sticker for sticker in stickers]    # 두번째 집부터 훔친경우
    mem2 = [sticker for sticker in stickers]    # 첫번째 집부터 훔친경우
    mem1[0], mem2[1] = 0, mem2[1]
    for i in range(2, len(stickers) - 1):
        mem1[i] = max(mem1[i - 1], mem1[i] + mem1[i - 2])
        mem2[i] = max(mem2[i - 1], mem2[i] + mem2[i - 2])
    mem1[-1] = max(mem1[-2], mem1[-1] + mem1[-3])
    mem2[-1] = max(mem2[-2], mem2[-3])
    return max(mem1[-1], mem2[-1])


def solution2(stickers):
    if len(stickers) < 3: return max(stickers)
    x1, x2, x3 = stickers[0], stickers[1], stickers[0] + stickers[2]    # 첫번째 집부터
    y1, y2, y3 = 0, stickers[1], stickers[2]                          # 두번째 집부터
    for sticker in stickers[3:]:
        x1, x2, x3 = x2, x3, max(x1, x2) + sticker
        y1, y2, y3 = y2, y3, max(y1, y2) + sticker
    return max(x1, x2, y2, y3)


print(solution([14, 6, 5, 11, 3, 9, 2, 10]))
print(solution2([14, 6, 5, 11, 3, 9, 2, 10]))