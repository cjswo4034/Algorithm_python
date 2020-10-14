import re


def solution(files):
    comp = re.compile('([^0-9]+)(\d+)')
    files.sort(key=lambda file: get_sort_keys(comp.findall(file)[0]))
    return files


def get_sort_keys(tuple):
    return tuple[0].lower(), int(tuple[1])


print(solution(["img12", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
