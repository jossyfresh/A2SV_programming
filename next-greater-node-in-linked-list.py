# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        stack = []
        ans = [0] * 10**4
        i = 0
        while head:
            while stack and stack[-1][0] < head.val:
                x = stack.pop()
                ans[x[1]] = head.val
            stack.append([head.val,i])
            head = head.next
            i += 1
        return ans[:i]