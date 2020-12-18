"""
Linked Lists -  single and double -  core operations: access, search, insert and delete. LL linked nodes to nodes

Single - Nodes linked in a one-way manner. Value to next_node, next location. Searching is better is nodes point to other nodes
        The first node is the head, last node is the tail. Next-node is linked list node(1, ...) The last or tail next node is None or another linked list.
        a = newNode(0, next=None)
        b = newNode(1, next=None)
        a.next = b

    insert = a=node(0), b=node(1), etc.
    head =a, move it to node 4, head is no longer a, its e. next =a
    b.next = e  e.next=c 
    insert and delete = O(1)

    access - 

Double - Nodes linked two-ways, head to tail and back.
Double the memory. Still have to go either way to get to the middle. Insert and delete are the same - O(n)
"""