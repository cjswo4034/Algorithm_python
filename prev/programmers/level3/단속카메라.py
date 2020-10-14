# def solution(routes):
#     routes = sorted(routes, key=lambda x: x[1])
#     last_camera = -30000
#
#     answer = 0
#
#     for route in routes:
#         if last_camera < route[0]:
#             answer += 1
#             last_camera = route[1]
#
#     return answer


def solution(routes):
    routes.sort(key=lambda x: (x[0], x[1]))

    ans = 0
    while routes:
        (l, r) = routes.pop(0)
        while routes and is_contain(routes[0], l, r):
            l = max(l, routes[0][0])
            r = min(r, routes[0][1])
            routes.pop(0)

        ans += 1
    return ans


def is_contain(route, l, r):
    return not (r <= route[0] or l >= route[1])


print(solution([[-20, 15], [-14, -5], [-18, -13], [-5, -3]]))
