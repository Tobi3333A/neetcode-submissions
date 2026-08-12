class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = list1
        curr2 = list2
        if not list1:
            curr3 = list2
            return curr3
        if not list2:
            curr3 = list1
            return curr3

        if list1.val < list2.val:
            head = list1
            curr3 = head
            curr1 = list1.next
        else:
            head = list2
            curr3 = head
            curr2 = list2.next

        while curr1 or curr2:
            if not curr2:
                curr3.next = curr1
                curr1 = curr1.next
            elif not curr1:
                curr3.next = curr2
                curr2 = curr2.next
            elif curr1.val < curr2.val:
                curr3.next = curr1
                curr1 = curr1.next
            else:
                curr3.next = curr2
                curr2 = curr2.next
            curr3 = curr3.next
        return head