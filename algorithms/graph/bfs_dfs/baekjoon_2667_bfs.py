"""
    <그림 1>과 같이 정사각형 모양의 지도가 있다.
    1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다.
    철수는 이 지도를 가지고 연결된 집의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다.
    여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다.
    대각선상에 집이 있는 경우는 연결된 것이 아니다.
    <그림 2>는 <그림 1>을 단지별로 번호를 붙인 것이다.
    지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.

    입력
    첫 번째 줄에는 지도의 크기 N(정사각형이므로 가로와 세로의 크기는 같으며 5≤N≤25)이 입력되고,
    그 다음 N줄에는 각각 N개의 자료(0혹은 1)가 입력된다.

    출력
    첫 번째 줄에는 총 단지수를 출력하시오. 그리고 각 단지내 집의 수를 오름차순으로 정렬하여 한 줄에 하나씩 출력하시오.

         <그림 1>                          <그림 2>
    0  1  1  0  1  0  0             0  1  1  0  2  0  0
    0  1  1  0  1  0  1             0  1  1  0  2  0  2
    1  1  1  0  1  0  1             1  1  1  0  2  0  2
    0  0  0  0  1  1  1             0  0  0  0  2  2  2
    0  1  0  0  0  0  0             0  3  0  0  0  0  0
    0  1  1  1  1  1  0             0  3  3  3  3  3  0
    0  1  1  1  0  0  0             0  3  3  3  0  0  0


    예제 입력                       예제 출력
    7                              3
    0110100                        7
    0110101                        8
    1110101                        9
    0000111
    0100000
    0111110
    0111000
"""
import io
import sys
from collections import deque

# n = 지도의 크기 (문제에서 지도는 정사각형 이므로 n x n)
# 연결된 집의 수 => 단지
# 단지수, 집의수 반환
def main():
    n = int(sys.stdin.readline().strip().split()[0])
    graph = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]

    row = len(graph)
    col = len(graph[0])

    visited = [[False] * col for _ in range(row)]

    def bfs(r, c):
        visited[r][c] = True
        queue = deque()
        queue.append((r,c))

        delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        house_cnt = 1

        while queue:
            cur_r, cur_c = queue.popleft()

            for dr, dc in delta:
                next_r = cur_r + dr
                next_c = cur_c + dc

                if 0 <= next_r < row and 0 <= next_c < col:
                    if not visited[next_r][next_c] and graph[next_r][next_c] == 1:
                        visited[next_r][next_c] = True
                        queue.append((next_r, next_c))
                        house_cnt += 1

        return house_cnt

    danzi_count = 0
    house_cnt_list = []
    for i in range(row):
        for j in range(col):
            if not visited[i][j] and graph[i][j] == 1:
                house_cnt_list.append(bfs(i, j))
                danzi_count += 1

    house_cnt_list.sort()  # 정렬

    print(danzi_count)
    for apt_cnt in house_cnt_list:
        print(apt_cnt)


test_input = """7
0110100
0110101
1110101
0000111
0100000
0111110
0111000
"""


sys.stdin = io.StringIO(test_input)  # 백준 제출 시 제거

main()