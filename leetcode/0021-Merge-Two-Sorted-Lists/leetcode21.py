class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1

        if l1.val < l2.val:
            start = dummy = l1
            l1 = l1.next
        else :
            start = dummy = l2
            l2 = l2.next

        while(l1.next and l2.next):
            if(l1.val > l2.val):
                dummy.next = l2
                l2 = l2.next
            else:
                dummy.next = l1
                l1 = l1.next
        dummy.next = l1 if l1 else l2
        return start.next