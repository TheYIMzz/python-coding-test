
import io
import sys

def main():

    n, m = map(int, sys.stdin.readline().split())

    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    visited = [False] * (n + 1)

    def dfs(graph, v, visited):
        visited[v] = True

        for next_v in graph[v]:
            if not visited[next_v]:
                dfs(graph, next_v, visited)

    count = 0
    for i in range(1, n + 1):
        if not visited[i]:
            dfs(graph, i, visited)
            count += 1
    print(visited)
    print(graph)
    print(count)

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
main()

sys.stdin = io.StringIO(test_input_2)
main()