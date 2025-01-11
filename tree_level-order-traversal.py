from collections import deque

class Node(object):
    def __init__(self):
        self.value = None
        self.left = None
        self.rigth = None


def level_order(root):
    visited = []

    if root is None:
        return 0 # root가 없으면 레벨 0

    q = deque()
    q.append(root)

    while q:
        cur_node = q.popleft() # 왼쪽부터 순회
        visited.append(cur_node.value) # 방문한 노드 추가

        if cur_node.left:
            q.append(cur_node.left) # 왼쪽 자식 노드
        if cur_node.right:
            q.append(cur_node.right) # 오른쪽 자식 노드

    return visited
