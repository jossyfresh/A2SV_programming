# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        i = 0
        temp = head 
        while temp!=None:
            temp = temp.next
            i+=1
        if n == 1:
            if head.next==None:
                head = None
                return head
            temp2 = head
            dhead = ListNode(0,None)
            dhead.next = temp2
            while temp2.next.next!=None:
                temp2 = temp2.next
            temp2.next = None
            return dhead.next
        else:
            if n==i:
                return head.next
            temp3 = head
            d2head = ListNode(0,None)
            d2head.next = temp3
            j = 0
            while j < i-(n+1):
                temp3 = temp3.next
                j+=1
            temp3.next = temp3.next.next
            return d2head.next