"""
    문제
        자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

        1부터 N까지 자연수 중에서 M개를 고른 수열
        같은 수를 여러 번 골라도 된다.
        고른 수열은 비내림차순이어야 한다.
        길이가 K인 수열 A가 A1 ≤ A2 ≤ ... ≤ AK-1 ≤ AK를 만족하면, 비내림차순이라고 한다.

    입력
        첫째 줄에 자연수 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)

    출력
        한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.

        수열은 사전 순으로 증가하는 순서로 출력해야 한다.

    예제 입력 1
     3 1
    예제 출력 1
        1
        2
        3
    예제 입력 2
        4 2
    예제 출력 2
        1 1
        1 2
        1 3
        1 4
        2 2
        2 3
        2 4
        3 3
        3 4
        4 4
    예제 입력 3
        3 3
    예제 출력 3
        1 1 1
        1 1 2
        1 1 3
        1 2 2
        1 2 3
        1 3 3
        2 2 2
        2 2 3
        2 3 3
        3 3 3
"""
import io, sys

# 중복허용 집합
def main():

    N, M = map(int, sys.stdin.readline().strip().split())

    result = []

    def back_track(start, curr):
        nonlocal result
        if len(curr) == M:
            result.append(curr[:])
            return

        for i in range(start, N + 1):
            curr.append(i)
            back_track(i, curr)
            curr.pop()

    back_track(1, [])

    for rst in result:
        print(" ".join(map(str, rst)))


sys.stdin = io.StringIO("""4 2""")
main()
