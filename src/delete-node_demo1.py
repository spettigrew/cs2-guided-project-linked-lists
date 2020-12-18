"""
Given only a reference to a specific node in a linked list, delete that node from a singly-linked list.

Example:

The code below should first construct a linked list (x -> y -> z) and then delete `y` from the linked list by calling the function `delete_node`. It is your job to write the `delete_node` function.

```python
class LinkedListNode():
    def __init__(self, value):
        self.value = value
        self.next  = None

x = LinkedListNode('X')
y = LinkedListNode('Y')
z = LinkedListNode('Z')

x.next = y
y.next = z

delete_node(y)
```

*Note: We can do this in O(1) time and space! But be aware that our solution will have some side effects...*
"""
class LinkedListNode():
    def __init__(self, value):
        self.value = value
        self.next  = None

def delete_node(delete_this_node):
    # Your code here
    # create a new variable pointing to z
    next_node = delete_this_node.next
        # copy all of next node into the current node we are 'deleting'
        # start with the value
    if next_node is not None:
        delete_this_node.value = next_node.value
        # skip over the next node in the linked_list
        delete_this_node.next = next_node.next # point from z (next_node) and go over to a
    else:
        print("Can't delete with this solution.")

    # cur_node.next.value - switch it to z
    # cur_node.next = None - takes off arrow to tail 'z'
    # cur_node.next.next - goes to node after 'old' z node



x = LinkedListNode('X')
y = LinkedListNode('Y')
z = LinkedListNode('Z')

x.next = y
y.next = z

delete_node(y)
