from typing import List, Dict, Set

class Node:
    def __init__(self, initial: int):
        self.initial = initial
        
        
def solution(emotions: List[int], orders: List[int]) -> List[int]:
    answer = [0] * len(orders)
    
    idx_map = {}
    key_map = {}
    nodes = [None] * (len(emotions) + 1)
    
    for i, emo in enumerate(emotions):
        node = Node(emo)
        idx_map.setdefault(emo, set()).add(node)
        key_map[node] = emo
        nodes[i + 1] = node

    curr = 1
    for order in orders:
        node = nodes[order]
        
        if node in key_map:
            prev_idx = key_map[node]
            bucket = idx_map.get(prev_idx)
            
            if bucket is not None:
                bucket.discard(node)
                if not bucket:
                    del idx_map[prev_idx]
            
            next_idx = curr + node.initial
            key_map[node] = next_idx
            idx_map.setdefault(next_idx, set()).add(node)
                
        # 현재 시점(curr)에서 만료될 노드들은 제거
        if curr in idx_map:
            for n in list(idx_map[curr]):
                key_map.pop(n, None)
            del idx_map[curr]
        
        # 현재 행복한 식물의 수
        answer[curr - 1] = len(key_map)
        curr += 1
    
    return answer

if __name__ == "__main__":
    print(solution([2, 3, 1, 2], [3, 1, 2, 1, 4, 1])) # [4, 2, 2, 2, 2, 1]
    print(solution([5, 5, 5], [1, 2, 1, 2, 3])) # [3, 3, 3, 3, 3]
    print(solution([5, 5, 5], [1, 2, 1, 2, 1])) # [3, 3, 3, 3, 2]
    print(solution([2, 1, 3, 4, 3], [2, 2, 2, 2, 5, 5, 5])) # [5, 4, 2, 1, 0, 0, 0]
    