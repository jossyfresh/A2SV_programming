# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dhead = ListNode(0,None)
        ddhead = ListNode(-1001,None)
        dhead.next = head
        ddhead.next = dhead
        x = -1000
        if head == None:
            return head
        while head.next != None:
            if head.val == head.next.val:
                x = head.val
                while head.next!=None and head.val == x:
                    head = head.next
                dhead.next = head
            else:
                head = head.next
                dhead = dhead.next
        if head.val == x:
            dhead.next = None
        return ddhead.next.next
        
            