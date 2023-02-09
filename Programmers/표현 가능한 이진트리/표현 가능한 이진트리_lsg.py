def solution(numbers):
    def get_sat_str(input_str):
        input_str = bin(num)[2:]  
        sat_len = 2 ** len(bin(len(input_str))[2:]) - 1
        padding_len = sat_len - len(input_str)
        return '0' * padding_len + input_str
    
    # 서브 트리를 재귀적으로 검사
    def check(res):
        # 부분 트리의 루트 노트 인덱스
        center = len(res) // 2
        # 루트노트를 표현할 수 없음
        if res[center] == '0':
            return 0
        # 리프 노드 도달
        if len(res) == 1:
            return 1
        left = res[:center]
        right = res[center+1:]
        # 왼쪽 서브 트리에 노드가 존재
        if '1' in left and not check(left):
            return 0
        # 오른쪽 서브 트리에 노드가 존재
        if '1' in right and not check(right):
            return 0
        return 1
        
    result = []
    for num in numbers: 
        sat_str = get_sat_str(num)
        result.append(check(sat_str))
        
    return result
