"""
    == 문제 ==
    문제에서 Binary 트리 하나와 해당 트리에 속한 두 개의 노드가 주어진다.
    이 때, 두 노드의 공통 조상 중 가장 낮은 node 즉, The Lowest Common Ancestor (LCA)를 찾아라
"""

class TreeNode:
    def __init__(self, left=None, right=None, value=None):
        self.left = left
        self.right = right
        self.value = value

# p와 q의 가장 가까운 노드 조상 값을 반환
def lca(cur_node, p, q):

    if cur_node is None:
        return None

    # 왼쪽, 오른쪽 서브트리에서 각각 LCA 탐색
    left = lca(cur_node.left, p, q)
    right = lca(cur_node.right, p, q)

    # 공통 조상을 찾기 위한 p와 q의 위치 찾기
    if cur_node == p or cur_node == q:
        return cur_node

    # 왼쪽, 오른쪽 서브트리 양쪽에서 노드가 반환되었다면 현재 노드가 p, q 의 공통조상
    elif left and right:
        return cur_node

    # 왼쪽이나 오른쪽 서브트리 한 곳에서만 p, q를 찾았으면 그쪽 결과 반환
    return left or right

# 예시 트리 구성
#         3
#       /   \
#      5     1
#     / \   / \
#    6   2 0   8
#       / \
#      7   4

root = TreeNode(value=3)

root.left = TreeNode(value=5)
root.left.left = TreeNode(value=6)
root.left.right = TreeNode(value=2)
root.left.right.left = TreeNode(value=7)
root.left.right.right = TreeNode(value=4)

root.right = TreeNode(value=1)
root.right.left = TreeNode(value=0)
root.right.right = TreeNode(value=8)

p = root.left
q = root.right

print("Lowest Common Ancestor:", lca(root, p, q).value)