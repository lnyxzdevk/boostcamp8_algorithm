def solution(numbers):
    answer = []

    for number in numbers:
        str_num = str(bin(number)[2:])
        str_num = make_tree_size(1,str_num)
        check = check_possible(str_num)
        answer.append(check)
    return answer

def check_possible(str_num):
    mid = len(str_num)//2
    if len(str_num) == 1:
        return 1
    if str_num[mid] == '0':
        return 0
    left_sub = str_num[:mid]
    right_sub = str_num[mid+1:]
    l=check_possible(left_sub)
    r=check_possible(right_sub)
    
    if '1' in left_sub and not l:
        return 0
    if '1' in right_sub and not r:
        return 0
    return 1

"0 1 0 1 0 1 0"


def make_tree_size(tree_size,str_num):
    if tree_size > len(str_num):
        str_num = '0'* (tree_size-len(str_num)) + str_num
        return str_num
    elif tree_size == len(str_num):
        return str_num
    else:
        return make_tree_size(((tree_size+1)*2-1),str_num)
    
        
