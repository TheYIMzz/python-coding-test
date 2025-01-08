class Node:
    def __init__(self, value=0, next_node=None):
        self.value = value
        self.next_node = next_node


first = Node(1)
second= Node(2)
third = Node(3)

first.next_node = second
second.next_node = third
first.value = 6


print('1번 노드 ', first)
print('2번 노드 ', second)
print('3번 노드 ', third)
print('1번 값 ', first.value)

print('1번 노드 ', first.next_node)
print('2번 노드 ', second.next_node)
print('3번 노드 ', third.next_node)
