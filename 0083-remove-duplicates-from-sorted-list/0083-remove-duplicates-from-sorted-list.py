# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dhead = ListNode(0,None)
        dhead.next = head
        if head == None:
            return head
        while head.next != None:
            if head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next
        return dhead.next
        