"""
    Tree 관련 개념
     1. 노드 (Node): 트리는 보통 노드로 구현된다.
     2. 간선 (Edge): 노드간에 연결된 선
     3. 루트 노드 (Root): 시작 노드. 트리는 항상 루트에서 시작한다.
     4. 리프 노드 (Leaf): 더 이상 뻗어나갈 수 없는 마지막 노드
     5. 자식 노드 (Child), 부모 노드(Parent), 형제 노드(Siblung)
     6. 차수 (degree): 각 노드가 갖는 자식의 수, 모든 노드의 차수가 n개 이하인 트리를 n진 트리라고 한다. (트리 안에서 가장 많은 자식을 가진 노드가 5개를 가지고 있다면 그 트리는 ‘5진 트리’)
     7. 조상 (ancestor): 위쪽으로 간선을 따라가면 만나는 모든 노드
     8. 자손 (descendant): 아래 쪽으로 간선을 따라가면 만나는 모든 노드
     9. 높이 (height): 루트 노드에서 가장 멀리있는 리프 노드 까지의 거리. 즉, 리프 노드 중에서 최대 레벨 값.
     10. 레벨 (level): 루트 노트에서 떨어진 거리
     11. 서브트리 (subtree): 루트 노드의 모든 자식(자손)들을 포함한 집합을 서브 트리
"""

class Node:
    def __init__(self, value = None, left = None, right = None):
        self.value = value
        self.left = left
        self.rigth = right

class BinaryTree:
    def __init_(self):
        self.root = None

bt = BinaryTree()
bt.root = Node(value = 1)
bt.root.left = Node(value = 2)
bt.root.rigth = Node(value = 3)

bt.root.left.left = Node(value = 4)
bt.root.left.right = Node(value = 5)

bt.root.rigth.right = Node(value = 6)
