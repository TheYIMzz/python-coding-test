
from collections import deque


##############
### bfs
def main():

    for idx, c in enumerate(computers):
        print(idx, c)


    visited = [False] * n

    def bfs(start):
        print('start: ', start)
        queue = deque()
        queue.append(start)
        visited[start] = True

        while queue:
            cur_v = queue.popleft()

            for j in range(n):
                if not visited[j] and computers[cur_v][j] == 1:
                    visited[j] = True
                    queue.append(j)


    network_cnt = 0
    for i in range(n):
        if not visited[i]:
            bfs(i)
            network_cnt += 1

    return network_cnt


###################
### dfs


def main():

    for idx, c in enumerate(computers):
        print(idx,c)

    visited = [False] * n

    def dfs(cur_v):
        visited[cur_v] = True

        for j in range(n):
            if not visited[j] and computers[cur_v][j] == 1:
                dfs(j)

    network_cnt = 0
    for i in range(n):
        if not visited[i]:
            dfs(i)
            network_cnt += 1

    return network_cnt

n = 3   # 컴퓨터 개수
computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]] # 연결정보
print(main())