# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return head
        curr = head
        purr = head
        lurr = head.next
        durr = head

        while durr:
            purr = lurr
            durr = lurr.next
            lurr.next = curr
            lurr = durr
            
            if curr == head:
                curr.next = None
            curr = purr
        return curr