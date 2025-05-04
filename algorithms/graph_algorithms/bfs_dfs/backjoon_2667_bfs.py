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

    n = int(input())
    graph = [list(map(int, input().strip())) for _ in range(n)]

    # print('n: ', n)
    # for i in graph:
    #     print('graph: ', i)

    row = len(graph)
    col = len(graph[0])

    visited = [[False] * col for _ in range(row)]

    def bfs(x, y, visited):
        print('==============')
        house_sum = 1
        delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        visited[x][y] = True
        queue = deque()
        queue.append((x, y))

        while queue:
            cur_x, cur_y = queue.popleft()
            print('방문 좌표: ', cur_x, cur_y)
            for dx, dy in delta:
                next_x = cur_x + dx
                next_y = cur_y + dy

                if next_x < row and next_x >= 0 and next_y < col and next_y >= 0:
                    if graph[next_x][next_y] == 1 and not visited[next_x][next_y]:
                        visited[next_x][next_y] = True
                        queue.append((next_x, next_y))
                        house_sum += 1
        return house_sum

    danji_sum = 0
    house_sums = []
    for i in range(row):
        for j in range(col):
            if graph[i][j] == 1 and not visited[i][j]:
                house_sums.append(bfs(i, j, visited))
                danji_sum += 1

    house_sums.sort() # 오름차순 정렬

    print(danji_sum)
    for house_sum in house_sums:
        print(house_sum)


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