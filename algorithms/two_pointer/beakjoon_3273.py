import io, sys
"""
    N이 최대 1,000,000이므로 
    최소 O(N)으로 풀어야하는 문제
    
    두 수의 합을 2중 for loop로 풀면 O(N^2)이 되어 연산횟수 10^11로 시간 초과
    O(N)은 O(10^5)로 안정적

"""

def solution():

    N = int(sys.stdin.readline().strip().split()[0])
    nums = list(map(int, sys.stdin.readline().strip().split()))
    X = int(sys.stdin.readline().strip().split()[0])
    nums.sort()

    print(N, nums, X)
    answer = 0

    left = 0
    right = N - 1

    while left < right:
        total = nums[left] + nums[right]

        if total == X:
            left += 1
            right -+ 1
            answer += 1
        elif total < X:
            left += 1
        else:
            right -= 1

    return answer

sys.stdin = io.StringIO("""9
5 12 7 10 9 1 2 3 11
13
""")

print(solution())
