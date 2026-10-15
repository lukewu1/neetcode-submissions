# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        newList = ListNode()
        curr = newList
        while list1 or list2:
            if not list1 and not list2:
                break
            elif not list1:
                curr.next = ListNode(list2.val)
                curr = curr.next
                list2 = list2.next
            elif not list2:
                curr.next = ListNode(list1.val)
                curr = curr.next
                list1 = list1.next
            else:
                if list1.val <= list2.val:
                    curr.next = ListNode(list1.val)
                    curr = curr.next
                    list1 = list1.next
                else:
                    curr.next = ListNode(list2.val)
                    curr = curr.next
                    list2 = list2.next
            
        return newList.next