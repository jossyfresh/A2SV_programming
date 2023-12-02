# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        arr.sort()
        dhead = ListNode()
        head = ListNode(arr[0])
        dhead.next = head
        for i in range(1,len(arr)):
            head.next = ListNode(arr[i])
            head = head.next
        return dhead.next