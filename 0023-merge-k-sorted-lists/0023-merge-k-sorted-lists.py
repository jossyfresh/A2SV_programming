# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nodes = []
        for x in lists:
            while x!=None:
                nodes.append(x.val)
                x = x.next
        nodes.sort()
        for i in range(len(nodes)):
            x = nodes[i]
            nodes[i] = ListNode(x,None)
        dhead = ListNode(0,None)
        if len(nodes) > 0:
            new = nodes[0]
            dhead.next = new
            for i in range(1,len(nodes)):
                new.next = nodes[i]
                new = new.next
            return dhead.next
        else:
            return dhead.next
        