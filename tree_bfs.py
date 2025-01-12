from collections import deque

"""
    BFS: Breadth-First Search 너비 우선 탐색 (Level Order Traversal)
"""
def bfs(root):
    visited = []  # 방문한 노드 저장

    if root is None:
        return 0

    q = deque()  # 방문 예정 노드 저장 (큐를 구현하기 위해 덱 자료구조 사용)
    q.append(root)

    while q:
        cur_node = q.popleft()
        visited.append(cur_node.value)

        if cur_node.left:
            q.append(cur_node.left)

        if cur_node.right:
            q.append(cur_node.right)

    return visited
