class MyCircularQueue:

    def __init__(self, k: int):
        self.front_pointer = 0
        self.rear_pointer = 0
        self.cir_queue = []

    def enQueue(self, value: int) -> bool:
        if (self.Rear == self.Front):
            return False
        else:
            self.cir_queue.append(value)
            return True

    def deQueue(self) -> bool:
        

    def Front(self) -> int:
        

    def Rear(self) -> int:
        

    def isEmpty(self) -> bool:
        

    def isFull(self) -> bool:
        return (self.Rear == self.Front)
            

# append -> Rear 추가 ()


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()