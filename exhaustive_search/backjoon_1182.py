"""
    문제
    N개의 정수로 이루어진 수열이 있을 때, 크기가 양수인 부분수열 중에서 그 수열의 원소를 다 더한 값이 S가 되는 경우의 수를 구하는 프로그램을 작성하시오.

    입력
    첫째 줄에 정수의 개수를 나타내는 N과 정수 S가 주어진다. (1 ≤ N ≤ 20, |S| ≤ 1,000,000) 둘째 줄에 N개의 정수가 빈 칸을 사이에 두고 주어진다.
    주어지는 정수의 절댓값은 100,000을 넘지 않는다.

    출력
    첫째 줄에 합이 S가 되는 부분수열의 개수를 출력한다.

    입력 예제
    5 0
    -7 -3 -2 5 8

    출력 예제
    1
"""
import io
import sys

test_input = """5 0
-7 -3 -2 5 8
"""

sys.stdin = io.StringIO(test_input)

n, s = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
count = 0

def back_track(start, curr):
    global count
    if sum(curr) == s and len(curr) > 0:  # len(curr) > 0 공집합 제외 조건
        count += 1

    for i in range(start, n):
        curr.append(nums[i])
        back_track(i + 1, curr)
        curr.pop()

back_track(start=0, curr=[])
print(count)