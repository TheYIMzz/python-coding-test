class Node:
    def __init__(self, value = 0, next_node = None):
        self.value = value
        self.next_node = next_node

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node

        else:
            self.tail.next = new_node
            self.tail = self.tail.next



ll = LinkedList()

ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
