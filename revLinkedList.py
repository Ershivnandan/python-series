# Definition for singly-linked list node
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_linked_list(head):
    prev = None
    current = head

    while current:
        next_node = current.next  # store next node
        current.next = prev       # reverse the current node's pointer
        prev = current            # move pointers one position ahead
        current = next_node
    
    return prev  # new head of the reversed list

# Helper function to print linked list
def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# Example usage:
# Creating a linked list: 1 -> 2 -> 3 -> None
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)

print("Original linked list:")
print_linked_list(head)

# Reversing the linked list
reversed_head = reverse_linked_list(head)

print("Reversed linked list:")
print_linked_list(reversed_head)
