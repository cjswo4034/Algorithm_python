def solution(n, arr1, arr2):
    answer = []
    for i, j in zip(arr1, arr2):
        answer.append(encode(i, j, n))

    # answer = []
    # for i, j in zip(arr1, arr2):
    #     res = str(bin(i|j)[2:])
    #     res = res.rjust(n, '0')
    #     res = res.replace('0', ' ')
    #     res = res.replace('1', '#')
    #     answer.append(res)

    return answer


def encode(value1, value2, length):
    result = int2bin(value1 | value2, length)\
        .replace('0', ' ')\
        .replace('1', '#')
    return result[len(result) - length:]


def int2bin(value, length):
    return format(value | (1 << length), 'b')


print(int2bin(9 | 30, 7))
print(solution(7, [9,20,28,18,11], [30,1,21,17,28]))

print(isinstance(bin(5|2)[2:], str))
print('12345'.rjust(7, '0'))