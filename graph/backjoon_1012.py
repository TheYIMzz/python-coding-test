"""
    차세대 영농인 한나는 강원도 고랭지에서 유기농 배추를 재배하기로 하였다.
    농약을 쓰지 않고 배추를 재배하려면 배추를 해충으로부터 보호하는 것이 중요하기 때문에, 한나는 해충 방지에 효과적인 배추흰지렁이를 구입하기로 결심한다.
    이 지렁이는 배추근처에 서식하며 해충을 잡아 먹음으로써 배추를 보호한다.
    특히, 어떤 배추에 배추흰지렁이가 한 마리라도 살고 있으면 이 지렁이는 인접한 다른 배추로 이동할 수 있어, 그 배추들 역시 해충으로부터 보호받을 수 있다.
    한 배추의 상하좌우 네 방향에 다른 배추가 위치한 경우에 서로 인접해있는 것이다.

    한나가 배추를 재배하는 땅은 고르지 못해서 배추를 군데군데 심어 놓았다.
    배추들이 모여있는 곳에는 배추흰지렁이가 한 마리만 있으면 되므로 서로 인접해있는 배추들이 몇 군데에 퍼져있는지 조사하면 총 몇 마리의 지렁이가 필요한지 알 수 있다.
    예를 들어 배추밭이 아래와 같이 구성되어 있으면 최소 5마리의 배추흰지렁이가 필요하다.
    0은 배추가 심어져 있지 않은 땅이고, 1은 배추가 심어져 있는 땅을 나타낸다.

    1	1	0	0	0	0	0	0	0	0
    0	1	0	0	0	0	0	0	0	0
    0	0	0	0	1	0	0	0	0	0
    0	0	0	0	1	0	0	0	0	0
    0	0	1	1	0	0	0	1	1	1
    0	0	0	0	1	0	0	1	1	1
"""
import io
import sys
from collections import deque


def main(graph, row, col):

    visited = [[False] * col for _ in range(row)]

    def bfs(x, y):
        visited[x][y] = True
        queue = deque()
        queue.append((x, y))

        delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while queue:
            cur_x, cur_y = queue.popleft()

            for dx, dy in delta:
                next_x = cur_x + dx
                next_y = cur_y + dy

                if next_x < row and next_x >= 0 and next_y < col and next_y >= 0:
                    if graph[next_x][next_y] == 1 and not visited[next_x][next_y]:
                        visited[next_x][next_y] = True
                        queue.append((next_x, next_y))


    worms_sum = 0
    for i in range(row):
        for j in range(col):
            if graph[i][j] == 1 and not visited[i][j]:
                bfs(i, j)
                worms_sum += 1
    return worms_sum


test_input = """2
10 8 17
0 0
1 0
1 1
4 2
4 3
4 5
2 4
3 4
7 4
8 4
9 4
7 5
8 5
9 5
7 6
8 6
9 6
10 10 1
5 5
"""
sys.stdin = io.StringIO(test_input)  # 백준 제출 시 제거

t = int(sys.stdin.readline())
results = []  # t 별로 저장할 결과

for _ in range(t):
    col, row, k = map(int, sys.stdin.readline().split())
    graph = [[0] * col for _ in range(row)] # 밭

    for _ in range(k):
        x, y = map(int, sys.stdin.readline().split())
        graph[y][x] = 1  # 밭의 배추 위치 설정 (파이썬 2차원 배열은 세로가 먼저, 가로가 나중이므로 [y][x])

    result = main(graph, row, col)
    results.append(result)

# 결과 출력
for res in results:
    print(res)

