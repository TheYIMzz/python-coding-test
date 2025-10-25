import io, sys

sys.setrecursionlimit(10**6)

def main():
    N = int(sys.stdin.readline().strip().split()[0])

    graph = [[0] for _ in range(N)]
    for i in range(N):
         graph[i] = list(map(int, sys.stdin.readline().strip().split()))

    max_h = max(map(max, graph))

    delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def dfs(r, c, high):

        visited[r][c] = True

        for dr, dc in delta:
            nr = dr + r
            nc = dc + c

            if 0 <= nr < N and 0 <= nc < N: # 그래프 범위 제한
                if not visited[nr][nc] and graph[nr][nc] > high:
                    visited[nr][nc] = True
                    dfs(nr, nc, high)

    result = 0
    for i in range(max_h + 1): # 높이 별 안전지대 덩어리 체크
        visited = [[False] * N for _ in range(N)]
        count = 0
        for y in range(N):
            for x in range(N):
                if not visited[y][x] and graph[y][x] > i:
                    dfs(y, x, i)
                    count += 1

        result = max(count, result) # count 와 result 중 더 큰 것으로 갱신

    print(result)

# sys.stdin = io.StringIO("""5
# 6 8 2 6 2
# 3 2 3 4 6
# 6 7 3 3 2
# 7 2 5 3 6
# 8 9 5 2 7""")

sys.stdin = io.StringIO("""7
9 9 9 9 9 9 9
9 2 1 2 1 2 9
9 1 8 7 8 1 9
9 2 7 9 7 2 9
9 1 8 7 8 1 9
9 2 1 2 1 2 9
9 9 9 9 9 9 9""")
main()








