from collections import deque


"""
    grid는 "1"(land)과 "0"(water)으로 이루어진 지도를 표현하는 m x n 이차원 배열이다. 이 지도에 표시된 섬들의 총 개수를 반환하시오.
    섬이란 수평과 수직으로 땅이 연결되어 있고 주변은 물로 둘러 쌓여있는 것을 말한다. 또한, grid의 네 개의 가장 자리는 모두 물로 둘러 쌓여있다고 가정한다.
    
    제약조건
        m == grid.length
        n == grid[i].length
        1 <= m, n <= 300
        grid[i][j] is '0' or '1'

"""
def num_is_island(grid):
    number_of_island = 0  # 섬의 개수

    row = len(grid)     # grid의 행(row)
    cal = len(grid[0])  # grid의 열(col)
    visited = [[False] * cal for _ in range(row)]  # grid와 동일한 크기의 2차원 배열 (방문 여부 추적용)

    def bfs(x, y):
        visited[x][y] = True  # 좌표 x, y값 방문 처리
        queue = deque()
        queue.append((x, y))  # 방문 처리된 좌표 탐색을 위해 좌표 q에 추가

        # 이동 시 좌표 상에서 x축 y축 값 +- 처리용 값 (상하 좌우 순서)
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        while queue:
            cur_x, cur_y = queue.popleft()

            for i in range(4):  # 상하좌우 반복
                next_x = cur_x + dx[i]
                next_y = cur_y + dy[i]

                # 방문하면 안되는 좌표 조건
                if next_x >= 0 and next_x < row and next_y >= 0 and next_y < cal:  # gred 범위를 벗어나지 않은 곳
                    if grid[next_x][next_y] == '1' and not visited[next_x][next_y]:  # 땅(1)인 곳, 방문하지 않은 곳
                        visited[next_x][next_y] = True
                        queue.append((next_x, next_y))

    # grid 순회 및 섬 개수 세기
    for i in range(row):
        for j in range(cal):
            if grid[i][j] == '1' and not visited[i][j]:  # 좌표에서 값이 1이고 방문하지 않았다면 BFS를 호출한다.
                bfs(i, j)
                number_of_island += 1

    return number_of_island



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


print(num_is_island(grid_2))