# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prevNode , curNode = None, head
        while curNode:
            
            nxt = curNode.next
            curNode.next = prevNode
            prevNode = curNode
            curNode = nxt
        return prevNode