"""
    문제
    통제 할 수 없는 미친 로봇이 평면위에 있다. 그리고 이 로봇은 N번의 행동을 취할 것이다.

    각 행동에서 로봇은 4개의 방향 중에 하나를 임의로 선택한다. 그리고 그 방향으로 한 칸 이동한다.

    로봇이 같은 곳을 한 번보다 많이 이동하지 않을 때, 로봇의 이동 경로가 단순하다고 한다. (로봇이 시작하는 위치가 처음 방문한 곳이다.) 로봇의 이동 경로가 단순할 확률을 구하는 프로그램을 작성하시오.
    예를 들어, EENE와 ENW는 단순하지만, ENWS와 WWWWSNE는 단순하지 않다. (E는 동, W는 서, N은 북, S는 남)

    입력
    첫째 줄에 N, 동쪽으로 이동할 확률, 서쪽으로 이동할 확률, 남쪽으로 이동할 확률, 북쪽으로 이동할 확률이 주어진다.
    N은 14보다 작거나 같은 자연수이고,
    모든 확률은 100보다 작거나 같은 자연수 또는 0이다.
    그리고, 동서남북으로 이동할 확률을 모두 더하면 100이다.

    확률의 단위는 %이다.

    출력
    첫째 줄에 로봇의 이동 경로가 단순할 확률을 출력한다. 절대/상대 오차는 10-9 까지 허용한다.


    예제 입력 1
    2 25 25 25 25
    예제 출력 1
    0.75

    예제 입력 2
    1 25 25 25 25
    예제 출력 2
    1.0

    예제 입력 3
    7 50 0 0 50
    예제 출력 3
    1.0

    예제 입력 4
    14 50 50 0 0
    예제 출력 4
    0.0001220703125

    예제 입력 5
    14 25 25 25 25
    예제 출력 5
    0.008845493197441101
"""
import io, sys


def main():

    n, east, west, south, north = map(int, sys.stdin.readline().strip().split())

    probs = [east/100, west/100, south/100, north/100]
    result = 0.0
    size = 2 * n + 1
    visited = [[False] * size for _ in range(size)]

    delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def back_track(r, c, depth, prob):
        nonlocal result

        if n == depth:
            result += prob
            print(f'깊이 {n} 도달 result 합산', result)# 제출 시 제거
            print(f'=============================================')# 제출 시 제거
            return
        print(f'현재 r 값: {r}')# 제출 시 제거
        print(f'현재 c 값: {c}')# 제출 시 제거
        for i, (dc, dr) in enumerate(delta):
            nr = r + dr
            nc = c + dc
            print()# 제출 시 제거
            print('for문 진입')# 제출 시 제거
            print(f'현재 i 값: {i}') # 제출 시 제거

            if visited[nr][nc]: # 제출 시 제거
                print('이미 방문한 노드: ', nr,nc) # 제출 시 제거

            if not visited[nr][nc]:
                visited[nr][nc] = True
                print('재귀호출에 넘겨줄 현재 확률값:', probs[i] * prob) # 제출 시 제거
                back_track(nr, nc, depth + 1, probs[i] * prob)
                visited[nr][nc] = False

    visited[n][n] = True
    back_track(n, n, 0, 1.0)  # 출발 지점에서 시작하므로 처음엔 존재할 확률 100%

    print(result)

sys.stdin = io.StringIO( # 제출 시 제거
"""2 25 25 25 25
""")

main()