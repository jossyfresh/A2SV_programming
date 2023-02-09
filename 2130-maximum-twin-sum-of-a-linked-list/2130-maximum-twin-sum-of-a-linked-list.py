# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        temp = head
        i = 0
        max_ = 0
        while temp!=None:
            temp = temp.next
            i+=1
        i = i//2
        pre = None
        cur = head
        nex = None
        while i > 0 :
            nex = cur.next  
            cur.next = pre 
            pre = cur 
            cur = nex
            i-=1
        while cur!=None:
            max_ = max(max_,cur.val+pre.val)
            cur =cur.next
            pre=pre.next
        return max_
            