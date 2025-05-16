from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    ## time complexity O(n)
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr is not None:
            next_pointer = curr.next
            curr.next = prev
            prev = curr
            curr = next_pointer

        return prev


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
    head = build_linked_list([1, 2, 3, 4, 5])
    reversed_head = solution.reverseList(head)
    print_linked_list(reversed_head)
