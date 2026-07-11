from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next 

class Solution:
    def reverse(self, head:Optional[ListNode]) -> Optional[ListNode]:        
        previous = None
        curr = head
        while curr:            
            next_temp = curr.next 
            curr.next = previous
            previous = curr
            curr = next_temp
        return previous



        

