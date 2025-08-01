"""
e.g.
58 -> 0111010 =  2+8+16+32
포화 이진트리로 이진수를 채워야함. 다만 더미 노드를 생성할 수 있으며, 해당 더미 노드는 0으로 채움
    포화 이진 트리: 1, 3, 7, 15 = 1, 1(+2), 1(+2+4), 1(+2+4+8), ...
    읽는 순서는 가장 왼쪽 리프노드부터 시작해서, 왼쪽 노드 -> 부모 노드 -> 우측 노드
[되는 경우] 7 -> 111
[되는 경우] 42 -> 32+8+2 -> 0101010 /
[되는 경우] 

[안되는 경우] 5 -> 101: 루트 노드가 0이되기 때문에 안됨
[안되는 경우] 95 -> 64+16+8+4+2+1 -> 1011111: 7개이지만 리프 노드의 부모 노드가 죽어버리므로 안됨(더미 노드를 추가하는건 되지만, 루트 노드는 그대로 유지해야함)

안되는 경우를 정리하면: 더미 노드를 붙여서 포화 이진 트리를 만들었을 때, 하나의 부모 노드라도 더미 노드가 되면 안됨

1의 부모 노드: 1
3의 부모 노드: 2
7의 부모 노드: 2, 4, 6
15의 부모 노드: 2, 4, 6, 8, 10, 12, 14
31의 부모 노드: 2, 4, 6, 8, 10, 12, 14, 16, 18, ... 30
...
즉, "xxxxxx"의 이진수에서, 짝수번째 번호가 0이되면 안되는 경우에 해당

더미 노드를 붙일 때는 원래 길이보다 딱 한 단계 더 길게 만들어야함 -> 길이 탐색
"""

def binary_search(search_area: list, target: int):
    left_idx, right_idx = 0, len(search_area)-1
    mid_idx = (right_idx + left_idx)//2
    
    while left_idx <= right_idx:
        if search_area[mid_idx] < target and search_area[mid_idx+1] > target:
            return search_area[mid_idx+1]
        
        if search_area[mid_idx] < target:
            left_idx = mid_idx + 1
        elif search_area[mid_idx] > target:
            right_idx = mid_idx - 1
    return


def solution(numbers):
    answer = []
    len_list = []
    curr_len = 1
    n = 1
    while curr_len <= 10000:
        len_list.append(curr_len)
        curr_len = curr_len + 2**n
        n += 1
    
    # 주어진 수를 이진수로 만들고, 이진 탐색을 통해 딱 한 단계 더 긴 길이로 만들기(더미 노드 추가)
    for num in numbers:
        curr_bin = bin(num)[2:]
        revised_length = binary_search(len_list, len(curr_bin))
        revised_curr_bin = "0"*(revised_length - len(curr_bin)) + curr_bin
            
        for i in range(len(revised_length)):
            if i%2 == 0 and revised_curr_bin[i] == '0':
                answer.append(0)
                break
    
    return answer

# test
print(solution([7, 42, 5])) # [1, 1, 0]
print(solution([63, 111, 95])) # [1, 1, 0]