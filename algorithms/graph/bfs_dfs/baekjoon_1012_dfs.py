import io
import sys

# 재귀 깊이 제한을 늘려줌
sys.setrecursionlimit(10**6)


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



def main(graph, col, row):
    visited = [[False] * col for _ in range(row)]

    def dfs(r, c):
        visited[r][c] = True
        delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for dr, dc in delta:
            next_r = dr + r
            next_c = dc + c

            if 0 <= next_r < row and 0 <= next_c < col:
                if not visited[next_r][next_c] and graph[next_r][next_c]:
                    dfs(next_r, next_c)

    count = 0
    for i in range(row):
        for j in range(col):
            if not visited[i][j] and graph[i][j] == 1:
                dfs(i, j)
                count += 1

    return count

#########################

t = int(sys.stdin.readline().strip().split()[0])

results = []
for _ in range(t):
    m, n, k = map(int, sys.stdin.readline().strip().split())
    graph = [[0] * m for _ in range(n)]

    for _ in range(k):
        x, y = map(int, sys.stdin.readline().strip().split())
        graph[y][x] = 1

    result = main(graph, m, n)
    results.append(result)

for res in results:
    print(res)