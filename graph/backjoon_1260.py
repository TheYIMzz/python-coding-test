"""
    그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오.
    단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고,
    더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

    입력
    첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다.
    다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다.
    어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다.
    입력으로 주어지는 간선은 양방향이다.

    출력
    첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다.
    V부터 방문된 점을 순서대로 출력하면 된다.

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
"""

import sys
import io
from collections import deque


def dfs(graph, v, visited, order):

    visited[v] = True
    order.append(v)
    
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
        order.append(cur_node)
        
        for next_node in graph[cur_node]:
            if not visited[next_node]:
                visited[next_node] = True
                queue.append(next_node)
    return order


def main():

    n, m, v = map(int, input().split())
    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    # 번호가 작은 정점(노드)을 먼저 방문하도록 인접 리스트를 오름차순 정렬
    print('정렬 전 그래프: ', graph)
    for sort_graph in graph:
        sort_graph.sort()  # sort_graph는 graph의 요소를 참조하기 때문에 graph의 요소가 정렬된다
    print('정렬 후 그래프: ', graph)

    # DFS 탐색
    visited_dfs = [False] * (n + 1)
    order_dfs = []
    dfs(graph, v, visited_dfs, order_dfs)

    # BFS 탐색
    order_bfs = bfs(graph, v)

    # 결과 출력 (각 정점을 공백으로 구분하여 한 줄에 출력)
    print(" ".join(map(str, order_dfs)))
    print(" ".join(map(str, order_bfs)))


test_input_1 = """4 5 1
1 2
1 3
1 4
2 4
3 4
"""

test_input_2 = """5 5 3
5 4
5 2
1 2
3 4
3 1
"""

sys.stdin = io.StringIO(test_input_1)  # 백준 제출 시 제거
main()
