"""
    그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오.
    단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고,
    더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

    입력 예제 1
        4 5 1
        1 2
        1 3
        1 4
        2 4
        3 4
    입력 예제 2
        5 5 3
        5 4
        5 2
        1 2
        3 4
        3 1

    ** 백준에서 문제 채점 시 입출력 방식 백준에 맞게 변경 필요 **
"""
import sys
from collections import deque

def main(n, m, v, vertext):
    """
    ### 백준 제출용 ###
    input = sys.stdin.read
    data = input().split("\n")

    # 첫 줄 입력값
    n, m, v = map(int, data[0].split())

    graph = [[] for _ in range(n + 1)]
    for i in range(1, m + 1):
        a, b = map(int, data[i].split())
        graph[a].append(b)
        graph[b].append(a)
    """

    graph = [[] for _ in range(n + 1)]

    for a, b in vertext:
        graph[a].append(b)
        graph[b].append(a)

    # 번호가 작은 정점(노드)을 먼저 방문하도록 인접 리스트를 오름차순 정렬
    print('정렬 전 그래프: ', graph)

    for sort_graph in graph:
        sort_graph.sort()
    print('정렬 후 그래프: ', graph)

    # DFS 탐색
    visited_dfs = [False] * (n + 1)
    order_dfs = []
    dfs(graph, v, visited_dfs, order_dfs)

    # BFS 탐색
    order_bfs = bfs(graph, v)

    """
    # 백준 제출용 결과 출력
    print(" ".join(map(str, dfs_result)))
    print(" ".join(map(str, bfs_result)))
    """
    return order_dfs, order_bfs

def dfs(graph, v, visited, order):
    visited[v] = True
    order.append(v)  # 방문한 정점(노드)들의 순서를 저장
    for next_node in graph[v]:
        if not visited[next_node]:
            dfs(graph, next_node, visited, order)


def bfs(graph, start):

    visited = [False] * len(graph)
    visited[start] = True
    queue = deque([start])

    order = []
    while queue:
        cur_node = queue.popleft()
        order.append(cur_node)  # 방문한 정점(노드)들의 순서를 저장
        for next_node in graph[cur_node]:
            if not visited[next_node]:
                visited[next_node] = True
                queue.append(next_node)

    return order


vertext = [[1, 2], [1, 3], [1, 4], [2, 4], [3, 4]]
vertext2 = [[5, 4], [5, 2], [1, 2], [3, 4], [3, 1]]

dfs_order, bfs_order = main(4, 5 , 1, vertext)
print('dfs_order: ', dfs_order)
print('bfs_order: ', bfs_order)

dfs_order2, bfs_order2 = main(5, 5 , 3, vertext2)
print('dfs_order2: ', dfs_order2)
print('bfs_order2: ', bfs_order2)
