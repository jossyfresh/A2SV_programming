# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        nodes = []
        temp = head
        while temp!=None:
            nodes.append(temp.val)
            temp = temp.next
        new = []
        j = 0
        x = []
        for i in range(len(nodes)):
            if j == k:
                new.append(x)
                x = []
                j = 0
            x.append(nodes[i])
            j+=1
        new.append(x)
        for i in range(len(new)):
            if len(new[i]) == k:
                new[i].reverse()
        ans = ListNode(new[0][0],None)
        dhead = ListNode(0,None)
        dhead.next = ans
        for x in new:
            for y in x:
                ans.next = ListNode(y,None)
                ans = ans.next
        return dhead.next.next
        
            