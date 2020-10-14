def solution(skill, skill_trees):
    skill_dic = {el: i for i, el in enumerate(skill)}

    answer = 0
    for skill_tree in skill_trees:
        skill_idx = get_skill_tree_idx(skill_dic, skill_tree)
        if is_ascending(skill_idx):
            answer += 1
    return answer


def get_skill_tree_idx(skill_dict, skill_tree):
    skill_idx = []
    for el in skill_tree:
        if skill_dict.get(el) is not None:
            skill_idx.append(skill_dict.get(el))
    return skill_idx


def is_ascending(skill_idx):
    return skill_idx == [i for i in range(skill_idx.__len__())]


print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))
