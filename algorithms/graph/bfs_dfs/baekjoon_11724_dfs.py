import io
import sys

sys.setrecursionlimit(10**7)

def main():
    n, m = map(int, sys.stdin.readline().strip().split())

    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        u, v = map(int, sys.stdin.readline().strip().split())
        graph[u].append(v)
        graph[v].append(u)

    def dfs(cur_node, visited):

        visited[cur_node] = True
        for next_node in graph[cur_node]:
            if not visited[next_node]:
                dfs(next_node, visited)

    visited = [False] * (n + 1)
    count = 0
    for i in range(1, n + 1):
        if not visited[i]:
            dfs(i, visited)
            count += 1

    print(visited)
    print(graph)

    return count

test_input = """6 5
1 2
2 5
5 1
3 4
4 6
"""

test_input_2 = """6 8
1 2
2 5
5 1
3 4
4 6
5 4
2 4
2 3
"""

sys.stdin = io.StringIO(test_input)
print(main())

sys.stdin = io.StringIO(test_input_2)
print(main())