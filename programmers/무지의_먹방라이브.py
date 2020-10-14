def solution(food_times, k):
    min_time, length = 0, len(food_times)
    food_time_with_idx = [[food_time, idx] for idx, food_time in enumerate(food_times)]
    food_time_with_idx = sorted(food_time_with_idx, key=lambda x: x[0])
    
    for i in range(length):
        if food_time_with_idx[i][0] == min_time: continue
        sub = (food_time_with_idx[i][0] - min_time) * (length - i)
        
        if k - sub < 0:
            tmp = sorted([ft[1] for ft in food_time_with_idx[i:]])
            return tmp[k % len(tmp)] + 1
        
        min_time = food_time_with_idx[i][0]
        k -= sub
        
    return -1
    
# 1. ft를 index와 묶어서 오름차순으로 정렬 (같을 시 index 오름차순)
# 2. 순회하면서 k -= (food_times[i] - min_idx) * (len(food_times) - i)

print(solution([5, 5, 5, 1, 5, 6, 7], 31))