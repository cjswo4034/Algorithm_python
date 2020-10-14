import math


def solution(progresses, speeds):
    answer = []
    remainder = list(map(lambda x, y: math.ceil((100 - x) / y), progresses, speeds))  # 1. (100 - progresses) / speeds

    j = 0
    for i in range(len(remainder)):
        if i < j:
            continue
        j = i + 1
        while j < len(remainder) and remainder[i] >= remainder[j]:
            j += 1
        answer.append(j - i)
    return answer


print(solution([93, 30, 55], [1, 30, 5]))

# def solution(progresses, speeds):
#     print(progresses)
#     print(speeds)
#     answer = []
#     time = 0
#     count = 0
#     while len(progresses)> 0:
#         if (progresses[0] + time*speeds[0]) >= 100:
#             progresses.pop(0)
#             speeds.pop(0)
#             count += 1
#         else:
#             if count > 0:
#                 answer.append(count)
#                 count = 0
#             time += 1
#     answer.append(count)
#     return answer

