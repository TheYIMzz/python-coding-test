"""
    문제
    N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.

    입력
    첫째 줄에 자연수 N(1 ≤ N ≤ 100,000)이 주어진다.
    다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다.
    다음 줄에는 M(1 ≤ M ≤ 100,000)이 주어진다.
    다음 줄에는 M개의 수들이 주어지는데, 이 수들이 A안에 존재하는지 알아내면 된다.
    모든 정수의 범위는 -231 보다 크거나 같고 231보다 작다.

    출력
    M개의 줄에 답을 출력한다. 존재하면 1을, 존재하지 않으면 0을 출력한다.

    입력 예제
    5
    4 1 5 2 3
    5
    1 3 7 9 5

    출력 예제
    1
    1
    0
    0
    1
"""

import sys
import io
import bisect

test_input = """5
4 1 5 2 3
5
1 3 7 9 5
"""
sys.stdin = io.StringIO(test_input)

n = int(sys.stdin.readline().strip())
n_nums = list(map(int, sys.stdin.readline().strip().split()))
m = int(sys.stdin.readline().strip())
m_nums = list(map(int, sys.stdin.readline().strip().split()))

n_nums.sort()  # 이분 탐색을 수행할 배열 정렬


# 이분탐색 직접 구현
def binary_search(a, x):

    # 탐색 구간
    lo = 0
    hi = len(a) - 1

    while lo <= hi:
        mid = (lo + hi) // 2  # 탐색 대상 List를 반으로 나눈다.

        if a[mid] < x:
            lo = mid + 1  # a[mid]가 x보다 작다 → x는 a의 중간값보다 크다 → 오른쪽 절반 탐색 (mid+1 … hi)
        else:
            hi = mid - 1  # a[mid]가 x보다 크다 → x는 a의 중간값보다 작다 → 왼쪽 절반 탐색 (lo … mid-1)

    return lo



def main():

    for num in m_nums:
        # idx = bisect.bisect_left(n_nums, num) # bisect 함수 사용
        idx = binary_search(n_nums, num)  # 직접구현 사용
        print(1 if idx < n and n_nums[idx] == num else 0)

main()

