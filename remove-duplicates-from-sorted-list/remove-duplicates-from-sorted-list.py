# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curN = head
        
        while curN:
            while curN.next and curN.val == curN.next.val:
                curN.next = curN.next.next
            curN = curN.next
        return head
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#                 curr_node = head
#         while curr_node:
#             while curr_node.next and curr_node.next.val == curr_node.val:
#                 curr_node.next = curr_node.next.next
#             curr_node = curr_node.next
#         return head