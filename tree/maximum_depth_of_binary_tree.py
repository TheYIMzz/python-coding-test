"""
    문제에서 주어진 binary tree의 최대 깊이를 반환
"""
from collections import deque


class TreeNode:
    def __init__(self, left=None, right=None, value=None):
        self.left = left
        self.right = right
        self.value = value

# level order 순회 방식 (너비 우선 탐색)
def max_depth_level_order(root):

    max_depth = 0

    if root is None:
        return 0

    q = deque()
    q.append((root, 1))  # 깊이 추적을 위해 튜플에 시작 노드와 깊이를 in queue (노드, depth)

    while q:
        cur_node, cur_depth = q.popleft()  # 큐에서 현재 노드와 깊이를 꺼낸다.

        max_depth = max(max_depth, cur_depth)  # 현재까지의 최대 깊이 업데이트

        if cur_node.left:
            q.append((cur_node.left, cur_depth + 1))  # 왼쪽 노드의 깊이 1 증가

        if cur_node.right:
            q.append((cur_node.right, cur_depth + 1))  # 오른쪽 노드의 깊이 1 증가

    return max_depth

# root = [3, 9, 20, None, 6, 15, 7]
root = TreeNode(value=3)

root.left = TreeNode(value=9)
root.right = TreeNode(value=20)

root.left.left = TreeNode(value=None)
root.left.right = TreeNode(value=6)

root.right.left = TreeNode(value=15)
root.right.right = TreeNode(value=7)

print('너비 우선 탐색 결과: ', max_depth_level_order(root))


######################################################################################

## Post order 순회 방식 (깊이 우선 탐색)
def max_depth_post_order(root):

    if root is None:
        return 0

    left_depth = max_depth_post_order(root.left)
    right_depth = max_depth_post_order(root.right)
    return max(left_depth, right_depth) + 1  # 깊이 +1 (가장 깊은 노드 도달 시 0을 반환하고 거기서부터 재귀호출한 노드마다 + 1)



root = TreeNode(value=3)

root.left = TreeNode(value=9)
root.right = TreeNode(value=20)

root.left.left = TreeNode(value=None)
root.left.right = TreeNode(value=6)

root.right.left = TreeNode(value=15)
root.right.right = TreeNode(value=7)

root.right.left.left = TreeNode(value=12)
root.right.left.right = TreeNode(value=84)

print('깊이 우선 탐색 결과: ', max_depth_post_order(root))
