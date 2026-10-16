# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        arr = []
        curr = head
        arr.append(curr)
        while curr.next:
            curr = curr.next
            arr.append(curr)

        arr[len(arr)//2].next = None
        l, r = 0, len(arr) - 1
        for i in range(len(arr)//2):
            arr[r].next = None
            arr[l].next = arr[r]
            arr.pop(r)
            l += 1
            r -= 1

        end = arr[0]
        for i in range(1, len(arr)):
            while end.next:
                end = end.next
            end.next = arr[i]
            