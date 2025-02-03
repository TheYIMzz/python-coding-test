"""
    grid는 "1"(land)과 "0"(water)으로 이루어진 지도를 표현하는 m x n 이차원 배열이다. 이 지도에 표시된 섬들의 총 개수를 반환하시오.
    섬이란 수평과 수직으로 땅이 연결되어 있고 주변은 물로 둘러 쌓여있는 것을 말한다. 또한, grid의 네 개의 가장 자리는 모두 물로 둘러 쌓여있다고 가정한다.

    제약조건
        m == grid.length
        n == grid[i].length
        1 <= m, n <= 300
        grid[i][j] is '0' or '1'

"""

def number_is_islands_dfs(grid):
    number_is_islands = 0

    row = len(grid)
    col = len(grid[0])

    visited = [[False] * col for _ in range(row)]

    def dfs(x, y):

        visited[x][y] = True

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]

            if next_x >= 0 and next_x < row and next_y >= 0 and next_y < col:
                if grid[next_x][next_y] == "1" and not visited[next_x][next_y]:
                    dfs(next_x, next_y)

    for i in range(row):
        for j in range(col):
            if grid[i][j] == "1" and not visited[i][j]:
                dfs(i, j)
                number_is_islands += 1

    return number_is_islands


grid_1 = [
    ['1', '1', '1', '1', '0'],
    ['1', '1', '0', '1', '0'],
    ['1', '1', '0', '0', '0'],
    ['0', '0', '0', '0', '0'],
]


grid_2 = [
    ['1', '1', '0', '0', '0'],
    ['1', '1', '0', '0', '0'],
    ['0', '0', '1', '0', '0'],
    ['0', '0', '0', '1', '1'],
]



print(number_is_islands_dfs(grid_2))