from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        ## set up left = current node and left previous
        dummy_head = ListNode(-1, head)
        left_prev , current_node = dummy_head, head

        for i in range(left-1):
            left_prev, current_node = current_node, current_node.next

        ## traverse and reverse
        prev = None
        for i in range(right -left +1):
            next_pointer = current_node.next
            current_node.next = prev
            prev, current_node = current_node, next_pointer

        ## update left prev to point to node after
        left_prev.next.next = current_node
        left_prev.next = prev
        return dummy_head.next
    

def build_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def print_linked_list(head):
    curr = head
    while curr:
        print(curr.val, end=" -> " if curr.next else "\n")
        curr = curr.next


if __name__ == "__main__":
    solution = Solution()
    head = build_linked_list([1,2,3,4,5] )
    left = 2
    right = 4
    reversed_head = solution.reverseBetween(head, left, right)
    print_linked_list(reversed_head)
