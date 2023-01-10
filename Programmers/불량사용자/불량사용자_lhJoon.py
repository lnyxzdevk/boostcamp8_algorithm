from itertools import permutations
def solution(user_id, banned_id):
    test = []
    results = list(permutations(user_id,len(banned_id)))
    # dfs 로 모든 경우 만들기.
    """
    def make_set(idx,tmp):
        if len(tmp) == len(banned_id):
            results.append(tmp)
            return
        if idx == len(user_id):
            return
        for i in range(len(user_id)):
            make_set(idx+1,tmp+[user_id[i]])
    """
    # 모든 경우 만들고 비교하기.     
    #make_set(0,[])
    #print(results)
    for sets in results:
        check = matching(sets,banned_id)
        if check:
            sets=list(sets)
            sets.sort()
            if sets not in test:
                test.append(sets)
    return len(test)

def matching(sample,target):
    # sample 과 target 이 리스트로 들어온다.
    i = 0
    check = True
    while i < len(sample):
        s = sample[i]
        t = target[i]
        if len(s) != len(t):
            check = False
            break
        for j in range(len(s)):
            if s[j] != t[j]:
                if t[j] != '*':
                    check = False
                    break
        i += 1
    return check
        