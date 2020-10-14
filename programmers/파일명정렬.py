import re

def solution(files):
    files = [[f, re.findall('([^\d]+)([\d]{1,5})', f)[0], i] for i, f in enumerate(files)]
    files = sorted(files, key=lambda f: (f[1][0].lower(), int(f[1][1]), f[2]))
    return [f[0] for f in files]

print(solution(["F-15"]))