# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr = l1
        num1 = 0
        count = 1
        while curr:
            num1 += (curr.val * count)
            count *= 10
            curr = curr.next
        
        curr = l2
        num2 = 0
        count = 1
        while curr:
            num2 += (curr.val * count)
            count *= 10
            curr = curr.next

        summ = num1 + num2
        head = ListNode()
        val = summ % 10
        head.val = val
        summ = summ // 10
        curr = head
        while summ > 0:
            val = summ % 10
            curr.next = ListNode(val)
            curr = curr.next
            summ = summ // 10
        
        return head