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
"""
1 2 3 4 5
1 3 7 9 5
"""
n = int(sys.stdin.readline().strip())
n_nums = list(map(int, sys.stdin.readline().strip().split()))
m = int(sys.stdin.readline().strip())
m_nums = list(map(int, sys.stdin.readline().strip().split()))

n_nums.sort()  # 이분 탐색을 수행할 배열 정렬

print('정렬된 n_nums (탐색 대상): ', n_nums)
print('찾을 m_nums 리스트: ', m_nums)

# 이분탐색 직접 구현
def binary_search(target_list, x):

    low = 0
    high = len(target_list) -1  # high를 len(target_list)로 잡고 mid를 (low + high) // 2로 계산하기 때문에 mid == len(target_list)이 나오면 인덱스 초과 오류로 -1한다.

    while low <= high:

        mid = (low + high) // 2

        # target_list[mid] == x가 성립하더라도 더 왼쪽 인덱스에 존재하는지 확인하기 위해 ==는 비교안함
        if target_list[mid] < x:  #  target_list[mid] 범위 초과 주의
            low = mid + 1
            print('mid: ', mid)
            print('low(mid + 1): ', low)
        else:
            high = mid - 1
            print('mid: ', mid)
            print('high(mid - 1): ', high)
    print('반환된 low 값: ', low)
    print()
    return low

def main():

    for num in m_nums:
        # idx = bisect.bisect_left(n_nums, num)
        idx = binary_search(n_nums, num)  # 직접구현 사용
        print(1 if idx < n and n_nums[idx] == num else 0)

main()



#########################################################
## 이분탐색 기본
def binary_search_exists(target_list, x):
    lo = 0
    hi = len(target_list) -1  # high를 len(target_list)로 잡고 mid를 (low + high) // 2로 계산하기 때문에 mid == len(target_list)이 나오면 인덱스 초과 오류로 -1한다.
    while lo <= hi:
        mid = (lo + hi) // 2
        if target_list[mid] == x:
            return True          # 찾았으니 바로 종료
        elif target_list[mid] < x:
            lo = mid + 1         # 오른쪽 절반으로
        else:
            hi = mid - 1       # 왼쪽 절반으로
    return False