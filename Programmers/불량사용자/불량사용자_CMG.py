from itertools import permutations

def check(perm, ban_id):
    for i in range(len(ban_id)):
        if len(perm[i]) != len(ban_id[i]):
            return False
        for p, b in zip(perm[i], ban_id[i]):
            if b == '*':
                continue
            if p != b:
                return False
    
    return True

def solution(user_id, banned_id):
    result = []
    
    for perm in permutations(user_id, len(banned_id)):
        if check(perm, banned_id):
            perm = set(perm)
            if perm not in result:
                result.append(perm)
    
    return len(result)
