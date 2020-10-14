def solution(N, stages):
    arr = [0] * (N + 2)
    for stage in stages:
        arr[stage] += 1

    fail_rates = []
    tot = len(stages)
    for i in range(1, len(arr) - 1):
        if tot == 0:
            fail_rates.append([0, i])
            tot -= arr[i]
        else:
            fail_rates.append([arr[i] / tot, i])

    fail_rates.sort(key=lambda x: (-x[0], x[1]))

    # answer = {}
    # div = len(stages)
    # for stage in range(1, N + 1):
    #     if div != 0:
    #         count = stages.count(stage)
    #         answer[stage] = count / div
    #         div -= count
    #     else:
    #         answer[stage] = 0
    # sorted(answer, key=lambda x: answer[x], reverse=True)

    return [fail_rate[1] for fail_rate in fail_rates]


print(solution(5, [2, 2, 2, 2, 2]))