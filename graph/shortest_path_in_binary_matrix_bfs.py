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

def shortest_patg_in_binary_matrix_bfs(grid):

    row = len(grid)
    low = len(grid[0])

    out_put = 0

    def bfs(x, y):
        pass

    for i in range(row):
        for j in range(low):
            if grid[i][j] == 0:
                bfs(i, j)

            elif grid[i][j] == 1:
                return -1

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

print(shortest_patg_in_binary_matrix_bfs(grid_1)) # output = 4
print(shortest_patg_in_binary_matrix_bfs(grid_2)) # output = -1