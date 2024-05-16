class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        # Create a new node
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.lenght = 1

my_linked_list = LinkedList(4)

print(my_linked_list.head.value)