class Node:
    def __init__(self, value = 0, next_node = None):
        self.value = value
        self.next_node = next_node

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, value):
        new_node = Node(value)

        if self.head is None:  # 리스트가 비어있는 경우
            self.head = new_node
            self.tail = new_node

        else:  # 리스트가 비어있지 않는 겨우
            self.tail.next_node = new_node  # 기존 노드의 next_node에 새 노드 연결
            self.tail = self.tail.next_node  # tail에 새 노드 연결

        self.size += 1

    def get(self, idx):
        if idx < 0 or idx > self.size: # index 0-base
            raise IndexError("Index out of range")

        current = self.head

        for i in range(idx):
            current = current.next_node

        return current.value



    def insert(self, idx, value):
        pass



    def delete(self, idx):
        pass


ll = LinkedList()

ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)

print('배열의 크기: ', ll.size)