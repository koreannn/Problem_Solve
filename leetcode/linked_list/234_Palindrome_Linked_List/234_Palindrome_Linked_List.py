# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
        
# class Solution:
#     def isPalindrome(self, head: ListNode) -> bool:
#         vals = []
#         while head:
#             vals.append(head.val)
#             head = head.next
#         return vals == vals[::-1]
    
# def Make_Linked_List(arr):
#         if not arr:
#             return None
#         head = ListNode(arr[0])
#         current = head
#         for val in arr[1:]:
#             current.next = ListNode(val)
#             current = current.next
#             return head
    
# Linked_List1 = Make_Linked_List([1,2,2,1])
# Linked_List2 = Make_Linked_List([1,2])

# # test
# print(Solution().isPalindrome(Linked_List1)) # True
# print(Solution().isPalindrome(Linked_List2)) # False

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        vals = []
        while head:
            vals.append(head.val)
            head = head.next
        return vals == vals[::-1]

# Helper function to create linked list from Python list
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Test cases
head1 = create_linked_list([1, 2, 2, 1])
head2 = create_linked_list([1, 2])

print(Solution().isPalindrome(head1))  # True
print(Solution().isPalindrome(head2))  # False