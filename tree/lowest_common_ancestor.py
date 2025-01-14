"""
    == 문제 ==
    문제에서 Binary 트리 하나와 해당 트리에 속한 두 개의 노드가 주어진다.
    이 때, 두 노드의 공통 조상 중 가장 낮은 node 즉, The Lowest Common Ancestor (LCA)를 찾아라
"""

# p와 q의 가장 가까운 노드 조상 값을 반환
def lca(cur_node, p, q):

    if cur_node is None:
        return None

    #  왼쪽, 오른쪽 서브트리에서 각각 LCA 탐색
    left = lca(cur_node.left, p, q)
    right = lca(cur_node.right, p, q)

    # 현재 노드가 p나 q라면 현재 노드를 반환 (자기 자신 노드도 조상으로 취급)
    if cur_node == p or cur_node == q:
        return cur_node

    #  왼쪽, 오른쪽 서브트리 양쪽에서 뭔가 찾았다면 지금 노드가 Lowest Common Ancestor
    elif left and right:
        return cur_node

    # 왼쪽 서브트리 쪽 혹은 오른쪽 서브트리 쪽에서만 찾았으면 그쪽 결과 반환
    return left or right
