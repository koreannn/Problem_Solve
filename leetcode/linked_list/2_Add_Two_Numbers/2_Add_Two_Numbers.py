# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers2(self, l1: list, l2: list) -> list:
        l1_origin = l1[::-1]
        l2_origin = l2[::-1]
        carry = 0
        max_length = len(l1_origin) if len(l1_origin)>len(l2_origin) else len(l2_origin)
        
        for i in range(max_length):
            
        
    def addTwoNumbers2(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        curr = dummy
        carry = 0
        
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0 # l1값이 남아있으면~
            val2 = l2.val if l2 else 0
            total = val1 + val2 + carry
            
            carry = total // 10
            curr.next = ListNode(total%10)
            curr = curr.next
            
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        return dummy.next


# test
print(Solution().addTwoNumbers([2,4,3], [5,6,4])) # [7,0,8]
print(Solution().addTwoNumbers([0], [0])) # [0]
print(Solution().addTwoNumbers([9,9,9,9,9,9,9], [9,9,9,9])) # [8,9,9,9,0,0,0,1]