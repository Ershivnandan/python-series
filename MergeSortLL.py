
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_sorted_lists(l1, l2):
    dummy = ListNode()
    tail = dummy

    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    if l1:
        tail.next = l1
    if l2:
        tail.next = l2

    return dummy.next


def split_list(head):
    if not head or not head.next:
        return head, None

    slow = head
    fast = head.next

    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    mid = slow.next
    slow.next = None 

    return head, mid


def sort_linked_list(head):
    if not head or not head.next:
        return head


    left, right = split_list(head)

   
    left = sort_linked_list(left)
    right = sort_linked_list(right)


    return merge_sorted_lists(left, right)


def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")


head = ListNode(4)
head.next = ListNode(2)
head.next.next = ListNode(1)
head.next.next.next = ListNode(3)

print("Original linked list:")
print_linked_list(head)

sorted_head = sort_linked_list(head)

print("Sorted linked list:")
print_linked_list(sorted_head)
