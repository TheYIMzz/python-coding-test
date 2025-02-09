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

    shortest_path_len  = -1

    row = len(grid)
    col = len(grid[0])

    if grid[0][0] != 0 or grid[row-1][col-1] != 0:
        return -1  # 시작 vertex가 0이 아니면 -1 반환

    visited = [[False] * col for _ in range(row)]
    queue = deque()

    visited[0][0] = True
    queue.append((0, 0, 1))

    delta = [(-1, 0), (1, 0), (0, -1), (0, 1),    # 동서남북
             (-1, -1), (1, -1), (1, 1), (-1, 1)]  # 대각선

    while queue:
        cur_x, cur_y, cur_len = queue.popleft()

        if cur_x == row -1 and cur_y == col - 1:   # 목적지 도착 시 예약된 큐 방문하지 않고 종료
            return cur_len  # 최단거리 반환

        for dx, dy in delta:
            next_x = cur_x + dx
            next_y = cur_y + dy

            if next_x >= 0 and next_x < row and next_y >= 0 and next_y < col:
                if grid[next_x][next_y] == 0 and not visited[next_x][next_y]:
                    visited[next_x][next_y] = True
                    queue.append((next_x, next_y, cur_len + 1))

    return shortest_path_len


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

grid_3 = [
        [0, 0, 0, 1, 0, 0, 0],
        [0, 1, 1, 1, 0, 1, 0],
        [0, 1, 0, 0, 0, 1, 0],
        [0, 0, 0, 1, 1, 1, 0],
        [0, 1, 0, 0, 0, 0, 0],
    ]


print(shortest_path_in_binary_matrix_bfs(grid_1)) # output => 4
print(shortest_path_in_binary_matrix_bfs(grid_2)) # output => -1
print(shortest_path_in_binary_matrix_bfs(grid_3)) # output => 9