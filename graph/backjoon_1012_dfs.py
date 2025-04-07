import io
import sys

# 재귀 깊이 제한을 늘려줌
sys.setrecursionlimit(10**6)

def main(graph, row, col):

    visited = [[False] * col for _ in range(row)]

    def dfs(graph, x, y, visited):
        visited[x][y] = True
        delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for dx, dy in delta:
            next_x = dx + x
            next_y = dy + y

            if 0 <= next_x < row and 0 <= next_y < col:
                if not visited[next_x][next_y] and graph[next_x][next_y] == 1:
                    dfs(graph, next_x, next_y, visited)


    result = 0

    for i in range(row):
        for j in range(col):
            if not visited[i][j] and graph[i][j] == 1:
                dfs(graph, i, j, visited)
                result += 1
    return result

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
results = []

for _ in range(t):

    col, row, k = map(int, sys.stdin.readline().split())
    graph = [[0] * col for _ in range(row)]

    for _ in range(k):
        x, y = map(int, sys.stdin.readline().split())
        graph[y][x] = 1

    result = main(graph, row, col)
    results.append(result)

# 결과 출력
for res in results:
    print(res)