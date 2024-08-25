from typing import Optional
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        prev = curr = head
        if curr.next:
            curr = curr.next
        
        while curr:
            if curr.val != prev.val:
                prev.next = curr
                prev = curr
            curr = curr.next
        prev.next = None
        
        return head


s = Solution()
print(s.deleteDuplicates([1, 1, 2]))
print(s.deleteDuplicates([1, 1, 2, 3, 3]))