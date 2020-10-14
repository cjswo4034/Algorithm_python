from math import floor
import re


def solution(str1, str2):
    str1 = [str1[i:i+2].lower() for i in range(len(str1) - 1) if not re.findall("[^a-zA-Z]+", str1[i:i+2])]
    str2 = [str2[i:i+2].lower() for i in range(len(str2) - 1) if not re.findall("[^a-zA-Z]+", str2[i:i+2])]

    str1, str2 = set(str1), set(str2)

    inter = str1.intersection(str2)
    union = str1.union(str2)

    if len(union) == 0: return 65536

    return floor(len(inter) / len(union) * 65536)


print(solution('aa1+aa2', '	AAAA12'))