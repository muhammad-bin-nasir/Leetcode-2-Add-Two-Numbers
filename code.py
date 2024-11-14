# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ptr1 = l1
        ptr2 = l2
        carry = 0
        res = ListNode()
        head = res
        
        while ptr1 is not None or ptr2 is not None or carry:
            val1 = ptr1.val if ptr1 else 0
            val2 = ptr2.val if ptr2 else 0
            
            total = val1 + val2 + carry
            carry = total // 10
            res.next = ListNode(total % 10)
            res = res.next
            
            if ptr1:
                ptr1 = ptr1.next
            if ptr2:
                ptr2 = ptr2.next
        
        return head.next
        
        
