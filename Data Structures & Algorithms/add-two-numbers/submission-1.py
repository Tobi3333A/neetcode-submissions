# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        num1 = 0
        mult = 1
        while l1:
            num1 += l1.val*mult
            l1 = l1.next
            mult*=10

        num2 = 0
        mult = 1
        while l2:
            num2 += l2.val*mult
            l2 = l2.next
            mult*=10

        addi = num1+num2

        divd = 10
        res = ListNode(addi%divd)
        addi = addi//divd
        head = res

        while addi:
            res.next = ListNode(addi%divd)
            addi = addi//divd
            res = res.next
        
        return head