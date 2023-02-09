# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        temp2 = head
        dhead = ListNode(0,None)
        dhead.next = temp
        i = 0
        while temp and temp.next != None:
            temp = temp.next
            i+=1
        i = (i+1)//2
        j = 0
        while j < i:
            temp.next = ListNode(temp2.next.val,None)
            temp = temp.next
            temp2.next = temp2.next.next
            temp2 = temp2.next
            j+=1
        return dhead.next
        