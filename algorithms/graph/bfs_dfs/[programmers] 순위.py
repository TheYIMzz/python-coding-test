from collections import deque


def main():

    win_graph = [[] for _ in range(n + 1)]
    loss_graph = [[] for _ in range(n + 1)]

    for u, v in results:
        win_graph[u].append(v)
        loss_graph[v].append(u)

    # for i in win_graph:
    #     print(i)
    # print()
    # for i in loss_graph:
    #     print(i)

    def bfs(start, graph):

        visited = [False] * (n + 1)
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
    for node in range(1, n + 1):
        win_result = bfs(node, win_graph)
        print(win_result)
        loss_result = bfs(node, loss_graph)
        print(loss_result)
        print(f'===== start: {node} =====')

        if win_result + loss_result == n - 1:
            answer += 1

    return answer
n = 5
results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
print(main())