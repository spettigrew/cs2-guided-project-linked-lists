"""
Given a reference to the head node of a singly-linked list, write a function
that reverses the linked list in place. The function should return the new head
of the reversed list.

In order to do this in O(1) space (in-place), you cannot make a new list, you
need to use the existing nodes.

In order to do this in O(n) time, you should only have to traverse the list
once.

*Note: If you get stuck, try drawing a picture of a small linked list and
running your function by hand. Does it actually work? Also, don't forget to
consider edge cases (like a list with only 1 or 0 elements).*
"""
class LinkedListNode():
    def __init__(self, value):
        self.value = value
        self.next  = None

def reverse(head_of_list):
    # Your code here
    # U - reverse the node direction 4->1. Head is now 4
    # set current node to new head, which is head_of_list
    cur_node = head_of_list
    prev_node = None
    next_node = None

    # make current node is not None
    while cur_node:
        # set the next node preserving access to next node
        # "cache" the next_node
        next_node = cur_node.next_node
        # make current node poin to previous node
        cur_node.next = prev_node  #which is currently None
        # shift cur and prev pointers to the right
        prev_node = cur_node 
        # move cur node to the next
        cur_node = next_node
    # return prev_node
    return prev_node

def print_list(head_of_list):
    # start at head as cur_node
    # iterate through list, printing the values
    current_node = head_of_list
    return_str = ''

    while current_node:
        return_str += f'({current_node.value}) -> '
        # move current_node forward
        current_node = current_node.next

    print(return_str)



    # cur_node point to prev_node
    # shift all 3 node pointers to the right
    # prev_node = cur_node
    # cur_node = next_node
    # next_node = cur_node.next
    # cur_node points to prev_node 



head = LinkedListNode(1)
head.next = LinkedListNode(2)
head.next.next = LinkedListNode(3)
head.next.next.next = LinkedListNode(4)