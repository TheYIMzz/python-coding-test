
from collections import deque


##############
### bfs
def main_bfs():

    for idx, c in enumerate(computers):
        print(idx, c)

    visited = [False] * n
    network_cnt = 0

    def bfs(start):

        queue = deque([start])
        visited[start] = True

        while queue:
            cur_v = queue.popleft()

            for connect_v in range(n):
                if not visited[connect_v] and computers[cur_v][connect_v] == 1:
                    visited[connect_v] = True
                    queue.append(connect_v)

    for i in range(n):
        if not visited[i]:
            bfs(i)
            network_cnt += 1

    return network_cnt


###################
### dfs
def main_dfs():

    for idx, c in enumerate(computers):
        print(idx,c)

    visited = [False] * n
    network_cnt = 0

    def dfs(cur_v):
        visited[cur_v] = True

        for connect_v in range(n):
            if not visited[connect_v] and computers[cur_v][connect_v] == 1:
                dfs(connect_v)

    for i in range(n):
        if not visited[i]:
            dfs(i)
            network_cnt += 1

    return network_cnt


n = 3   # 컴퓨터 개수
computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]] # 연결정보
print(main_bfs())
print(main_dfs())