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

    입력 예제 3
        1000 1 1000
        999 1000

    출력 예제 1
        1 2 4 3
        1 2 3 4

    출력 예쩨 2
        3 1 2 5 4
        3 1 4 2 5

    출력 예제 3
        1000 999
        1000 999
"""

import sys
import io
from collections import deque



def main():
    n, m, v = map(int, sys.stdin.readline().strip().split())

    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        a, b = map(int, sys.stdin.readline().strip().split())
        graph[a].append(b)
        graph[b].append(a)

    for sorted_graph in graph:
        sorted_graph.sort()



    def dfs(start, visited, result_node):
        visited.add(start)
        result_node.append(start)

        for next_v in graph[start]:
            if next_v not in visited:
                dfs(next_v, visited, result_node)
        return result_node


    def bfs(start, visited):
        visited[start] = True
        queue = deque()
        queue.append(start)

        resunt_node = []
        while queue:
            cur_node = queue.popleft()

            resunt_node.append(cur_node)
            for next_node in graph[cur_node]:
                if not visited[next_node]:
                    visited[next_node] = True
                    queue.append(next_node)

        return resunt_node


    result_node = []
    dfs_result = dfs(v, set(), result_node)

    bfs_visited = [False] * (n + 1)
    bfs_result = bfs(v, bfs_visited)

    print(" ".join(map(str, dfs_result)))
    print(" ".join(map(str,bfs_result)))

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

test_input_3 = """1000 1 1000
999 1000
"""

sys.stdin = io.StringIO(test_input_1)  # 백준 제출 시 제거
main()
