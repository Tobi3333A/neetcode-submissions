# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        count = 0
        while curr:
            count += 1
            curr = curr.next
        pos = count - n

        curr = head
        prev = None
        for i in range(pos+1):
            if i == pos:
                if not prev:
                    return curr.next
                prev.next = curr.next
                break

            prev = curr
            curr = curr.next
        
        return head