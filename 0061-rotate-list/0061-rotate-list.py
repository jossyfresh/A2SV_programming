# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None:
            return head
        elif head.next == None:
            return head
        nodes = []
        temp1=  head
        while temp1!=None:
            nodes.append(ListNode(temp1.val,None))
            temp1 = temp1.next
        if k == 0 or k%len(nodes)==0:
            return head
        k = k % len(nodes)
        k = len(nodes)-k
        ans = nodes[k]
        dhead = ListNode(0,None)
        dhead.next = ans 
        j = k+1
        while j < len(nodes):
            ans.next = nodes[j]
            ans = ans.next
            j+=1
        i = 0
        while i < k:
            ans.next = nodes[i]
            ans = ans.next
            i+=1
        return dhead.next
            