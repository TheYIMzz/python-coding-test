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
import sys
import io
sys.setrecursionlimit(10**7)


test_input = """2 25 25 25 25
"""
sys.stdin = io.StringIO(test_input)

n, east, west, south, north = map(int, sys.stdin.readline().strip().split())
probs = [east/100, west/100, south/100, north/100]


def main():

    result = 0.0

    size = 2 * n + 1
    visited = [[False] * size for _ in range(size)]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def back_track(x, y, depth, prob):

        nonlocal result

        if depth == n:
            result += prob
            return

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not visited[nx][ny]:
                visited[nx][ny] = True
                back_track(nx, ny, depth + 1, prob * probs[i])
                visited[nx][ny] = False


    visited[n][n] = True
    back_track(n, n, 0, 1.0)
    print(result)


main()