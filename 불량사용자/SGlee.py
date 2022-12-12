from collections import Counter

def solution(user_id, banned_id):
    def dps(depth, id_candidate, stack, answer_list, flag_set):
        if depth == len(banned_id):
            answer_list.append(tuple(sorted(stack)))
            return 
        for c_id in id_candidate[depth]:
            if c_id not in flag_set:
                stack.append(c_id)
                flag_set.add(c_id)
                dps(depth + 1, id_candidate, stack, answer_list, flag_set)
                stack.pop()
                flag_set.remove(c_id)

    def check(uid, bid):
        if len(uid) != len(bid):
            return False
        else:
            return all([a == b or b == '*' for a, b in zip(uid, bid)])
    
    id_candidate = []
    for b_id in banned_id:
        candiate = [u_id for u_id in user_id if check(u_id, b_id)]
        id_candidate.append(candiate)

    answer_list = []
    dps(0, id_candidate, [], answer_list, set())
    
    return len(set(answer_list))
