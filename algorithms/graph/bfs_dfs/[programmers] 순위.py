from collections import deque


def main():

    win_graph = [[] for _ in range(n + 1)]
    loss_graph = [[] for _ in range(n + 1)]

    win_visited = [False] * (n + 1)
    loss_visited = [False] * (n + 1)

    for u, v in results:
        win_graph[u].append(v)
        loss_graph[v].append(u)

    for i in win_graph:
        print(i)
    print()
    for i in loss_graph:
        print(i)

    def bfs(start, visited, graph):
        visited[start] = True
        queue = deque()
        queue.append(start)
        count = 0
        while queue:
            cur_v = queue.popleft()

            for next_v in graph[cur_v]:
                if not visited[next_v]:
                    visited[next_v] = True
                    queue.append(next_v)
                    count += 1
        return count

    answer = 0

    for i in range(1, n + 1):
        win_result = bfs(i, win_visited, win_graph)
        loss_result = bfs(i, loss_visited, loss_graph)

        if win_result + loss_result == n - 1:
            answer += 1

    return answer
n = 5
results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
print(main())