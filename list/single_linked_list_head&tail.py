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

        if idx < 0 or idx > self.size:
            raise IndexError("Index out of range")

        new_node = Node(value)

        if self.head is None:  # 리스트가 비어있는 경우
            self.head = new_node
            self.tail = new_node

        else:
            if idx == 0:  # 0번쨰 삽입 시
                new_node.next_node = self.head
                self.head = new_node

            elif idx == self.size:  # 맨 끝 삽입 시
                self.tail.next_node = new_node  # tail의 다음 노드를 삽입된 노드로 변경
                self.tail = new_node  # tail을 새 노드로 변경

            else: # 중간 삽입 시
                cur_node = self.head

                for i in range(idx -1):
                    cur_node = cur_node.next_node

                new_node.next_node = cur_node.next_node
                cur_node.next_node = new_node
        self.size += 1

    def delete(self, idx):

        if idx < 0 or idx > self.size:
            raise IndexError("Index out of range")

        if idx == 0: # 맨앞 삭제
            remove_node = self.head
            self.head =  self.head.next_node
            if self.size == 1:  # 삭제하려고 보니 노드가 1개만 있다면
                self.tail = None

        else: # 중간, 테일 삭제
            cur_node = self.head
            for i in range(idx -1):
                cur_node = cur_node.next_node
            remove_node = cur_node.next_node
            cur_node.next_node = cur_node.next_node.next_node

            if remove_node == self.tail:
                self.tail = cur_node

        self.size -= 1
        return print('삭제된 노드: ', remove_node.value)


ll = LinkedList()
print('=== append ===')
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
print('배열의 크기: ', ll.size)

print('=== get ===')
print(ll.get(0))
print(ll.get(1))
print(ll.get(2))
print(ll.get(3))


print('=== insert ===')
ll.insert(0, '0 헤드 삽입')
ll.insert(2, '2 중간 삽입')
ll.insert(6, '6 테일 삽입')
print(ll.get(0))
print(ll.get(1))
print(ll.get(2))
print(ll.get(3))
print(ll.get(4))
print(ll.get(5))
print(ll.get(6))


print('=== delete ===')
ll.delete(6)
ll.delete(2)
ll.delete(0)
print(ll.get(0))
print(ll.get(1))
print(ll.get(2))
print(ll.get(3))