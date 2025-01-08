class MyHashMap:

    def __init__(self):
        self.size = 1009
        self.table = [[] for _ in range(self.size)]

    def put(self, key: int, value: int) -> None:
        hash_key = key % self.size
        
        # 체이닝 방식으로 저장
        for pair in self.table[hash_key]:
            if pair[0] == key:
                pair[1] = value # 기존 값을 업데이트
                return
        self.table[hash_key].append([key, value]) # 기존에 있던 값이 없으면 새로운 값을 추가

    def get(self, key: int) -> int:
        hash_key = key % self.size
        
        for pair in self.table[hash_key]:
            if pair[0] == key:
                return pair[1]
        return -1 # 값이 없을 경우

    def remove(self, key: int) -> None:
        hash_key = key % self.size
        
        for i, pair in enumerate(self.table[hash_key]):
            if pair[0] == key:
                del self.table[hash_key][i]
                return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)