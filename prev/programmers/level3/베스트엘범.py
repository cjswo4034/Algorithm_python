class MusicInfo:
    def __init__(self, idx, play):
        self.idx = idx
        self.play = play


def solution(genres, plays):
    # 1. 장르별로 음악 정보 저장하는 dict
    # 2. 장르별로 재생 횟수 저장하는 list [genre, play]
    # 3. 2.에 대해 play 순으로 내림차순
    # 4. 3.을 순회하며 1.에서 리스트를 꺼내서 answer 에 저장
    answer = []
    music_counts = dict()
    music_infos = dict()
    for i in range(len(genres)):
        if music_infos.get(genres[i]) is None:
            music_infos[genres[i]] = []
            music_counts[genres[i]] = 0
        music_infos[genres[i]].append(MusicInfo(i, plays[i]))
        music_counts[genres[i]] = music_counts[genres[i]] + plays[i]

    for genre, _ in sorted(music_counts.items(), key=lambda x: -x[1]):
        arr = sorted(music_infos[genre], key=lambda music_info: (-music_info.play, music_info.idx))
        answer.append(arr[0].idx)
        if len(arr) > 1:
            answer.append(arr[1].idx)
    return answer


print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))

