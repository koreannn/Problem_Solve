class MyCircularDeque:

    def __init__(self, k: int):
        self.queue = [0]*k
        self.head = 0
        self.rear = 0
        self.capacity = len(self.queue) # k
        self.size = 0 # 현재 요소 개수

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.queue[self.head] = value
        self.head = (self.head+1) % self.capacity
        self.size = self.size + 1
        return True

    def insertLast(self, value: int) -> bool:
        

    def deleteFront(self) -> bool:
        

    def deleteLast(self) -> bool:
        

    def getFront(self) -> int:
        

    def getRear(self) -> int:
        

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()