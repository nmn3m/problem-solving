class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    ## time complexity O(n)
    def middleNode(self, head):
        slow = fast = head 
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


def build_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


if __name__ == '__main__':
    solution = Solution()
    head = build_linked_list([1, 2, 3, 4, 5])
    middle_node = solution.middleNode(head)
    print(middle_node.val)  
