# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        i = 0
        temp1 = head
        while temp1.next!=None:
            temp1 = temp1.next
            i+=1
        temp = ListNode(temp1.val,None)
        temp2 = ListNode(0,None)
        temp2.next = temp
        temp1 = head
        n = i
        new = []
        while n > 0:
            temp1 = head
            i = 0
            while i < n-1:
                temp1 = temp1.next
                i+=1
            n-=1
            new.append(ListNode(temp1.val,None))
            
        for x in new:
            temp.next = x
            temp = temp.next
        return temp2.next
        
        
        