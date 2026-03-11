import random

class RandomizedSet:
    def __init__(self):
        self.data_list = []
        self.data_map = {} 

    def insert(self, val: int) -> bool:
        if val in self.data_map:
            return False
        self.data_map[val] = len(self.data_list) # {val: idx} 형태로 저장
        self.data_list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.data_map:
            return False
        idx = self.data_map[val] # 삭제하고자 하는 값의 인덱스
        last_val = self.data_list[-1] # 삭제하고자 하는 값
        
        self.data_list[idx] = last_val
        self.data_map[last_val] = idx
        
        self.data_list.pop()
        del self.data_map[val]
        return True
        
    def getRandom(self) -> int:
        return random.choice(self.data_list)

# test
obj = RandomizedSet()
obj.insert(1)
obj.remove(2)
obj.insert(2)
obj.getRandom()
obj.remove(1)
obj.insert(2)
obj.getRandom()

"""
문제를 빠르게 이해하는 방법 - 입출력 예시를 먼저 본다
해시셋을 다루는 방법(메서드 등)
최적화
defaultdict?
30분동안은 절대 AI안쓰고 스스로 생각하고 고민하기
"""
