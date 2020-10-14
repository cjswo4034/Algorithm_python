def solution(p,n):
    # 1. p -> 24시간으로 고친다.
    p = p_to_24(p)

    # 2. n -> 시 분 초로 고친다.
    n = n_to_24(n)

    # 3. p + n 을 초부터 조정한다.
    time = [0, 0, 0]
    for i in range(2, -1, -1):
        time[i] += p[i] + n[i]
        if i != 0:
            pp, r = divmod(time[i], 60)
            time[i - 1] += pp
            time[i] = str(r).zfill(2)

    # 4. 시간을 24로 나눈다.
    time[0] = str(time[0] % 24).zfill(2)
    return ':'.join(time)


def p_to_24(p):
    p = p.split(" ")
    h, m, s = map(int, p[1].split(":"))
    if h >= 12: h -= 12
    if p[0] == 'PM': h += 12
    return h, m, s


def n_to_24(n):
    h, n = divmod(n, 3600)
    m, s = divmod(n, 60)
    return h, m, s


print(solution("AM 12:00:00", 1))