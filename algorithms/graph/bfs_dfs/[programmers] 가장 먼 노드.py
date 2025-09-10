from collections import deque

def main():

    graph = [[] for _ in range(n + 1)]

    for u, v in vertex:
        graph[u].append(v)
        graph[v].append(u)

    visited = [-1] * (n + 1)
    queue = deque([1])
    visited[1] = 1

    while queue:
        cur_v = queue.popleft()

        for next_v in graph[cur_v]:
            if visited[next_v] == -1:
                visited[next_v] = visited[cur_v] + 1
                queue.append(next_v)

    max_depth = max(visited)
    return visited.count(max_depth)

n = 6
vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
print(main())