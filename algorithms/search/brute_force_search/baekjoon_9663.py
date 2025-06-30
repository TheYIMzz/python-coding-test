"""
    문제
        N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.
        N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.

    입력
        첫째 줄에 N이 주어진다. (1 ≤ N < 15)

    출력
        첫째 줄에 퀸 N개를 서로 공격할 수 없게 놓는 경우의 수를 출력한다.

    예제 입력 1
        8
    예제 출력 1
        92

"""
import io, sys


def main():
    N = int(sys.stdin.readline().strip())

    count = 0                           # 퀸을 모두 배치한 경우의 수를 세기 위한 변수
    col_used = [False] * N              # 같은 열에 퀸이 이미 있는지 체크
    diag1_used = [False] * (2 * N - 1)  # ↘ 방향 대각선(오른쪽 아래 대각선)에 퀸이 있는지 체크
    diag2_used = [False] * (2 * N - 1)  # ↙ 방향 대각선(왼쪽 아래 대각선)에 퀸이 있는지 체크

    def backtrack(row):
        nonlocal count

        if row == N:  # 퀸을 N개 전부 정상적으로 배치한 경우에 +1
            count += 1
            return

        for col in range(N):
            if col_used[col] or diag1_used[row + col] or diag2_used[row - col + N - 1]:
                continue

            col_used[col] = diag1_used[row + col] = diag2_used[row - col + N - 1] = True
            backtrack(row + 1)
            col_used[col] = diag1_used[row + col] = diag2_used[row - col + N - 1] = False

    backtrack(0)
    print(count)



sys.stdin = io.StringIO("""8""")
main()