def solution(n, arr1, arr2):
    answer = [bin(e1 | e2)[2:].rjust(n, '0') for e1, e2 in zip(arr1, arr2)]
    answer = [e.replace('1', '#').replace('0', ' ') for e in answer]
    return answer