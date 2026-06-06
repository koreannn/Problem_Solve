def solution(s):
    answer = 0
    curr_first = None
    first_cnt = 0
    else_cnt = 0
    
    for char in s:
        # 새로운 부분이 시작되는 경우 첫 글자 지정
        if curr_first is None:
            curr_first = char
            first_cnt = 1
            continue
        
        if char == curr_first:
            first_cnt += 1
        else:
            else_cnt += 1
        
        if first_cnt == else_cnt:
            answer += 1
            curr_first = None
            first_cnt = 0
            else_cnt = 0
    
    if curr_first is not None:
        answer += 1
    
    return answer