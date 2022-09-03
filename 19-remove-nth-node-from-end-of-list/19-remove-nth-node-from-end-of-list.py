# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next == None:
            return None
        slow = head
        fast = head
        for _ in range(n):
            fast = fast.next
        prev_node = head
        while fast:
            prev_node = slow
            slow = slow.next
            fast = fast.next
        if slow == head:
            head = slow.next
        else:
            prev_node.next = slow.next
        return head
        