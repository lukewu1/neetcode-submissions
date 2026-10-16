# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        length = 1
        sentinel = head
        curr = head
        prev = None
        while curr.next:
            prev = curr
            curr = curr.next
            length += 1
        
        if length <= 1:
            return
    
        prev.next = None
        curr.next = sentinel.next
        sentinel.next = curr
        sentinel = curr.next

        numSwaps = 1
        while numSwaps != (length//2):
            temp = prev
            prev = curr
            curr = temp
            while prev.next != curr:
                prev = prev.next

            prev.next = None
            curr.next = sentinel.next
            sentinel.next = curr 
            sentinel = curr.next
            numSwaps += 1

        return