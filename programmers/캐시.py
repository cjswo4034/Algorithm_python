from collections import deque

def solution(cacheSize, cities):
    if cacheSize == 0: return len(cities) * 5
    answer = 0
    cache = deque(maxlen=cacheSize)
    for city in cities:
        city = city.lower()
        if city in cache:
            cache.remove(city)
            cache.append(city)
            answer += 1
        else:
            cache.append(city)
            answer += 5
    return answer

# LRU: 최근 가장 조금 사용한
# 캐시에 저장되어 있으면 해당 도시를 맨 뒤로 : cash hit
# 캐시에 저장되어 있지 않으면) cash miss
#  1. 공간이 있다면 맨 뒤에 push
#  2. 공간이 없다면 맨 앞 pop and 도시 push