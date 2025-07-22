from collections import deque


def main():

    graph = [[] for _ in range(n + 1)]
    visited = [False] * (n + 1)
    dist = [0] * (n + 1)

    for u, v in vertex:
        graph[u].append(v)
        graph[v].append(u)

    queue = deque()
    queue.append(1)
    visited[1] = True

    while queue:
        cur_v = queue.popleft()

        for next_v in graph[cur_v]:
            if not visited[next_v]:
                visited[next_v] = True
                dist[next_v] = dist[cur_v] + 1
                queue.append(next_v)

    max_dist = max(dist)
    return dist.count(max_dist)

n = 6
vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
print(main())