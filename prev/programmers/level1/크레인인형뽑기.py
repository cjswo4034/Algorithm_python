def solution(boards, moves):
    stacks = [[] for _ in range(len(boards))]
    for i in range(len(boards)):
        for j in range(len(boards)):
            if boards[i][j]:
                stacks[j].append(boards[i][j])

    stack, answer = [], 0
    for move in moves:
        if not stacks[move - 1]: continue
        tmp = stacks[move - 1].pop(0)
        if stack and stack[-1] == tmp:
            answer += 2
            stack.pop()
        else:
            stack.append(tmp)
    print(stacks)

    return answer


print(solution(
    [[0,0,0,0,0],
     [0,0,1,0,3],
     [0,2,5,0,1],
     [4,2,4,4,2],
     [3,5,1,3,1]], [1,5,3,5,1,2,1,4]	))