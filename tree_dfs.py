"""
    DFS: Depth-First Search 깊이 우선 탐색
"""
def dfs(cur_node):
    if cur_node is None:
        return

    dfs(cur_node.left)
    dfs(cur_node.right)

"""
 전위 순회(preorder)
"""
def preorder(cur_node):
    if cur_node is None:
        return

    print(cur_node.value)  # 전위 순회(preorder) 방문
    dfs(cur_node.left)
    dfs(cur_node.right)

"""
 중위 순회(inorder)
"""
def inorder(cur_node):
    if cur_node is None:
        return


    dfs(cur_node.left)
    print(cur_node.value)  # 중위 순회(inorder) 방문
    dfs(cur_node.right)

"""
 후위 순회(postorder)
"""
def postorder(cur_node):
    if cur_node is None:
        return

    dfs(cur_node.left)
    dfs(cur_node.right)
    print(cur_node.value)  # 후위 순회(postorder) 방문