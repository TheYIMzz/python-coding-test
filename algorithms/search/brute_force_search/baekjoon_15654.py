"""
    문제
    N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오. N개의 자연수는 모두 다른 수이다.

    N개의 자연수 중에서 M개를 고른 수열
    입력
    첫째 줄에 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)

    둘째 줄에 N개의 수가 주어진다. 입력으로 주어지는 수는 10,000보다 작거나 같은 자연수이다.

    출력
    한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.

    수열은 사전 순으로 증가하는 순서로 출력해야 한다.

    예제 입력 1
    3 1
    4 5 2
    예제 출력 1
    2
    4
    5
    예제 입력 2
    4 2
    9 8 7 1
    예제 출력 2
    1 7
    1 8
    1 9
    7 1
    7 8
    7 9
    8 1
    8 7
    8 9
    9 1
    9 7
    9 8
"""
import io, sys


def main():

    N, M = map(int, sys.stdin.readline().strip().split())
    nums = list(map(int, sys.stdin.readline().strip().split()))
    nums.sort()
    result = []
    def back_track(curr):
        nonlocal result

        if len(curr) == M:
            result.append(curr[:])
            return

        for num in nums:
            if num not in curr:
                curr.append(num)
                back_track(curr)
                curr.pop()

    back_track([])
    for rst in result:
        print(" ".join(map(str, rst)))

sys.stdin = io.StringIO("""4 2
9 8 7 1""")
main()