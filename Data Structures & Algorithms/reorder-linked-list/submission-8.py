# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        curr = slow.next
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        slow.next = None

        first, second = head, prev
        while second:
            t1, t2 = first.next, second.next
            first.next = second
            second.next = t1
            first, second = t1, t2


            