"""
문제
어떤 큰 도화지에 그림이 그려져 있을 때, 그 그림의 개수와, 그 그림 중 넓이가 가장 넓은 것의 넓이를 출력하여라. 단, 그림이라는 것은 1로 연결된 것을 한 그림이라고 정의하자. 가로나 세로로 연결된 것은 연결이 된 것이고 대각선으로 연결이 된 것은 떨어진 그림이다. 그림의 넓이란 그림에 포함된 1의 개수이다.

입력
첫째 줄에 도화지의 세로 크기 n(1 ≤ n ≤ 500)과 가로 크기 m(1 ≤ m ≤ 500)이 차례로 주어진다. 두 번째 줄부터 n+1 줄 까지 그림의 정보가 주어진다. (단 그림의 정보는 0과 1이 공백을 두고 주어지며, 0은 색칠이 안된 부분, 1은 색칠이 된 부분을 의미한다)

출력
첫째 줄에는 그림의 개수, 둘째 줄에는 그 중 가장 넓은 그림의 넓이를 출력하여라. 단, 그림이 하나도 없는 경우에는 가장 넓은 그림의 넓이는 0이다.

예제 입력 1
6 5
1 1 0 1 1
0 1 1 0 0
0 0 0 0 0
1 0 1 1 1
0 0 1 1 1
0 0 1 1 1
예제 출력 1
4
9
"""


import io, sys
sys.setrecursionlimit(10**7)  # 최대 재귀 깊이 한도 증가 (미 설정 시 백준 런타임에러, bfs 추천)

def main():

    N, M = map(int, sys.stdin.readline().strip().split())

    graph = []
    for _ in range(N):
        graph.append(list(map(int, sys.stdin.readline().strip().split())))

    visited = [[False] * M for _ in range(N)]
    delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def dfs(r, c):

        visited[r][c] = True
        count = 1

        for dr, dc in delta:
            nr = dr + r
            nc = dc + c

            if 0 <= nr < N and 0 <= nc < M:
                if not visited[nr][nc] and graph[nr][nc] == 1:
                    count += dfs(nr, nc)

        return count

    picture_size_list = []
    picture_cnt = 0

    for i in range(N):
        for j in range(M):
            if not visited[i][j] and graph[i][j] == 1:
                picture_size_list.append(dfs(i, j))
                picture_cnt += 1

    print(picture_cnt)
    print(max(picture_size_list, default=0))

sys.stdin = io.StringIO("""6 5
1 1 0 1 1
0 1 1 0 0
0 0 0 0 0
1 0 1 1 1
0 0 1 1 1
0 0 1 1 1
""")
main()