class Node:
    def __init__(self, value = 0, next_node = None):
        self.value = value
        self.next_node = next_node

class LinkedList(object):
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node # 헤드가 없을 때만 new_node를 가리킴

        else:
            current = self.head # head에 접근 (linked list에 접근하기 위함)
            while current.next_node: # 마지막 노드(next가 None)까지 가는 반복문
                current = current.next_node
            current.next_node = new_node # 마지막 노드가 None 이면 반복문 빠져나와서 마지막 노드 뒤에 새로운 노드 주소값 추가

    def get(self, idx):
        current = self.head # head에 접근 (linked list에 접근하기 위함)
        for i in range(idx):
            current = current.next_node
        return current.value

    def insert(self, idx, value):
        new_node = Node(value)

        if idx == 0: # 맨 앞에 삽입 시
            new_node.next_node = self.head # 헤드 노드를 새로운 노드 다음 노드로 지정
            self.head = new_node # 새로운 노드를 헤드로 지정

        else:
            current = self.head # 중간 삽입 시 헤드 노드부터 접근

            for i in range(idx -1): # 새로운 노드를 삽입하기 직전까지 이동
                current = current.next_node

            new_node.next_node = current.next_node # 새로운 노드에 현재 노드의 다음 노드 주소 값을 넣어주고
            current.next_node = new_node # 현재 노드에 새로운 노드를 연결

    def delete(self, idx):
        if idx == 0:
            self.head = self.head.next_node # 0 번째(head)를 삭제하면 다음 노드를 head로 설정한다.
        else:
            current = self.head

            for i in range(idx -1):
                current = current.next_node
            current.next_node = current.next_node.next_node # 현재 노드의 다음 노드를 다음 다음 노드로 변경 (가비지 컬렉터가 참조안하는 인덱스 삭제해줌)



ll = LinkedList()

"""
append
"""
print("== append 값: 1 - 4 ==")
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)

"""
get
"""
print("== get 함수 ==")
print(ll.get(0))
print(ll.get(1))
print(ll.get(2))
print(ll.get(3))

"""
insert
"""
print("== insert 함수 ==")
ll.insert(0, '( 0번쨰에 insert Node )')
print(ll.get(0))
print(ll.get(1))
print(ll.get(2))
print(ll.get(3))
print(ll.get(4))

"""
delete
"""
print("== delete 함수 ==")
ll.delete(0)
print(ll.get(0))
print(ll.get(1))
print(ll.get(2))
print(ll.get(3))
