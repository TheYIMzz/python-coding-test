"""
    n x n binary mattix인 grid가 주어졌을 때, 출발지에서 목적지까지 도착하는 가장 빠른 경로의 길이를 반환하시오.
    만약 경로가 없다면 -1을 반환하시오.

    출발지: top-left cell
    목적지: bottom-right cell

        - 값이 0인 cell 끼리만 지나갈 수 있다
        - cell 끼리는 8가지 방향으로 연결되어 있다. (edge와 corner 방향으로 총 8가지 이다. => 대각선까지)
        - 연결된 cell을 통해서만 지나갈 수 있다.

    제약 조건
        - n == grid.length
        - n == grid[i].length
        - 1 <= n <= 100
        - grid[i][j] is 0 or 1
"""
from collections import deque


def shortest_path_in_binary_matrix_bfs(grid):
    # print(grid)
    row = len(grid)
    col = len(grid[0])

    out_put = 0

    visited = [[False] * col for _ in range(row)]


    def bfs(x, y):
        print('현재 좌표: ', x, y)
        queue = deque()
        queue.append((x, y))

        dx = [1, 1, -1, 1, 0, 0]
        dy = [1, -1, 0, 0, -1, 1]

        while queue:
            cur_x, cur_y = queue.popleft()

            for i in range(5):

                next_x = cur_x + dx[i]
                next_y = cur_y + dy[i]

                if next_x == 0 and next_x < row and next_y == 0 and next_y < col:
                    if not visited[next_x][next_y]:
                        visited[x][y] = True
                        queue.append((next_x, next_y))

    if grid[0][0] == 1:
        return -1

    for i in range(row):
        for j in range(col):
            if grid[i][j] == 0 and not visited[i][j]:

                bfs(i, j)
                out_put += 1

    return out_put


grid_1 = [
        [0, 0, 0],
        [1, 1, 0],
        [1, 1, 0],
    ]

grid_2 = [
        [1, 0, 0],
        [1, 1, 0],
        [1, 1, 0],
    ]

print(shortest_path_in_binary_matrix_bfs(grid_1)) # output = 4
print(shortest_path_in_binary_matrix_bfs(grid_2)) # output = -1