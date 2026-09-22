# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        elif not list2:
            return list1

        if list1.val < list2.val:
            list3 = list1
            list1 = list1.next
        else:
            list3 = list2
            list2 = list2.next

        head = list3

        while list1 or list2:
            if not list1:
                list3.next = list2
                break
            elif not list2:
                list3.next = list1
                break
            elif list1.val < list2.val:
                list3.next = list1
                list1 = list1.next
                list3 = list3.next
            else:
                list3.next = list2
                list2 = list2.next
                list3 = list3.next

        return head