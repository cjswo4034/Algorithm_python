def solution(cacheSize, cities):
    if cacheSize == 0: return len(cities) * 5
    answer = 0
    cache = []
    while cities:
        city = cities.pop(0).lower()
        if city in cache:
            answer += 1
            cache.remove(city)
        else:
            answer += 5
            if cacheSize == len(cache): cache.pop(0)
        cache.append(city)
        print(cache)
    return answer


print(solution(3, ["Jeju", "Jeju", "Jeju", "Jeju", "Jeju", "Jeju"]))