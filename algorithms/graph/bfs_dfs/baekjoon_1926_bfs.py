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
from collections import deque

def main():


    N, M = map(int, sys.stdin.readline().strip().split())
    # N = 세로, M 가로
    graph = []

    for _ in range(N):
        graph.append(list(map(int, sys.stdin.readline().strip().split())))


    visited = [[False] * M for _ in range(N)]

    def bfs(r, c):
        queue = deque()

        visited[r][c] = True
        queue.append((r, c))

        delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        count = 1
        while queue:
            cur_r, cur_c = queue.popleft()

            for dr, dc in delta:
                next_r = dr + cur_r
                next_c = dc + cur_c

                if 0 <= next_r < N and 0 <= next_c < M:
                    if not visited[next_r][next_c] and graph[next_r][next_c] == 1:
                        visited[next_r][next_c] = True
                        count += 1
                        queue.append((next_r, next_c))
        return count

    picture_size_list = []
    picture_cnt = 0

    for i in range(N):
        for j in range(M):
            if not visited[i][j] and graph[i][j] == 1:
                result = bfs(i, j)
                picture_size_list.append(result)
                picture_cnt += 1

    print(picture_cnt)
    print(max(picture_size_list, default=0))  # 그림이 하나도 없는 경우 Null이 되므로 오류 방지 기본 값 0

sys.stdin = io.StringIO("""6 5
1 1 0 1 1
0 1 1 0 0
0 0 0 0 0
1 0 1 1 1
0 0 1 1 1
0 0 1 1 1
""")
main()